# Feedback for Claude — Recruitment / hiring-stage access (after Grok 103–108)

Independent review. Use this to decide what goes on any public work/applying-for-a-job page, what stays internal, and what becomes a line in the existing FOI companion log. It is research constraint, not page copy. Do not paste Grok output onto the hub. Do not turn this batch into advice on any named person's live application.

**Date:** 14 September 2026
**Files behind this:**
- `Recruitment-prompt-103-definitions-legal-status.md`
- `Recruitment-prompt-104-who-pays-who-books-failures.md`
- `Recruitment-prompt-105-pre-employment-health-questionnaires.md`
- `Recruitment-prompt-106-international-comparative.md`
- `Recruitment-prompt-107-lived-experience-case-for-change.md`
- `Recruitment-prompt-108-agency-platform-duty-holder.md`
- `Recruitment-prompts-103-108-claude-feedback.md` (Grok's own self-review, 13 September 2026 — read in full before this pass)
- `Recruitment-prompt-170-murphy-sheffield-hallam-transcript-verification.md` (Grok, 14 September 2026 — verification-only patch, see resolved addendum below)
- `Murphy-v-Sheffield-Hallam-EAT-6-99-1101.rtf` (human-downloaded BAILII transcript, 14 September 2026 — independently read in full for this update, not just Grok's write-up of it)

Re-open before publish — GOV.UK CSI page (`apply-for-communication-support-at-a-job-interview…`, last updated 8 Oct 2025); AtW staff-guide HTML CSI-hours paragraph (2 vs 3 hours, contested); ACAS *Following discrimination law – Recruitment* and *Interviewing job applicants* (both dated 30 Jun 2026 on the original pass); EHRC pre-employment health questions pages; Elite Careplus investigation page.

This batch is the pre-employment door: application form, shortlist, interview interpreter, s.60 questionnaire. It answers "can they get in," not "what happens once they are in." Distinct from 20–26/27–33 (benefits, Jobcentre), 52–54 (in-work AtW cap/waits), 92–96 (OH after an offer), 97–102 (in-post HR/IT ticket), 109–114 (grievance after a missed ticket).

**Proposed domain:** stub under Welfare & Employment cluster. Do **not** stand up a new Domain off this batch.

---

## Verdict for any public page

**Curate first. Draft almost nothing.**

Grok's own self-review already reaches this verdict and does it well — the per-prompt source register and Don't list are unusually disciplined for this batch, and the two spot-checks below did not disturb the headline. The one sentence a page is allowed to lead with, if any:

> An employer (and a recruitment agency) must adjust the recruitment process for a disabled applicant — including a BSL or deafblind interpreter at interview — unless that step is not reasonable on the facts. Access to Work Communication Support at Interview (CSI) is a separate, candidate-applied, 100% funded fast-track. It does not move the Equality Act duty. General health questions before a job offer are banned except for named exceptions; asking whether someone needs an adjustment *for this interview* is one of those exceptions.

What already exists and should be linked, not rewritten:

| Need | Point at |
|---|---|
| Process-adjustment duty at application/interview | Equality Act ss.20, 39, 55. ACAS *Following discrimination law – Recruitment* and *Interviewing job applicants* (30 Jun 2026). EHRC Employment Code ch. 16. |
| Who pays / CSI product | GOV.UK *Apply for communication support at a job interview* — spot-checked live 14 Sep 2026, holds verbatim (see below). |
| Pre-offer health questions | EA s.60. EHRC employer + applicant s.60 guides. Elite Careplus Ltd investigation (EHRC, 2021). |
| Booking lead time (market, not statute) | BDF hearing-loss briefing: 2–4 weeks. Rearrange rather than proceed without. |
| Agency is not a post-box | EA ss.55–56, 109–111. REC Code principle 4. Employment Code 10.48 agency example. |

Thin original drafts worth doing *later*, after a human signs this file off — unchanged from Grok's own review, which already scoped these correctly:

1. A one-screen "two routes, one duty" card (Route A employer/agency books and pays; Route B candidate applies for CSI). England/Scotland/Wales badge, no NI.
2. A four-line invitation sentence an employer or agency can paste, clearly labelled as a suggestion, not official ACAS text.
3. FOI questions folded into the existing companion log (see ranked list below). Not a new tracker.

Do not write a second CSI explainer — GOV.UK already owns the form.

---

## Spot-check results (14 September 2026 pass)

Two load-bearing claims re-verified live rather than trusted from the quote, per this project's sourcing standard.

**1. GOV.UK CSI page — holds verbatim.** Fetched live 14 September 2026. Confirms: candidate (not employer) applies, before the interview; 100% of approved costs, no cost-share, "does not have to be paid back and will not affect your other benefits"; paid *after* the interview; applicant must supply employer name, interview date, expected duration, employer contact, and total cost. Page's own "last updated" date is **8 October 2025** (the October 2025 edit removed textphone details in favour of Relay UK) — this matches what both prompt 104 and Grok's self-review already state. No drift found. The CSI-hours cap (2 vs 3 hours) remains genuinely unresolved on this pass — the live staff-guide HTML paragraph was not re-opened end-to-end, so that specific figure stays contested exactly as Grok flagged it. Do not resolve it by picking one number for public copy.

**2. Murphy v Sheffield Hallam University — now fully resolved. See "Resolved" section below; the paragraphs that follow are kept for the audit trail of how this was chased down, not as the current caveat.**

Original spot-check (14 Sep, before the transcript was obtained): searched and fetched the swarb.co.uk case note live. It confirmed the claimant was profoundly deaf, no signer was arranged for the original interview, the interview was rearranged, the case was decided under the Disability Discrimination Act 1995 (not the Equality Act 2010), and the appeal on the appointment question failed — but swarb's note did not itself state the £2,500 award, the 16/18 December 1997 dates, or the "amateur signer" detail. Those specifics rested on Grok's original citation alone at that point, with no second primary source.

---

## RESOLVED — Murphy v Sheffield Hallam transcript obtained and independently verified, 14 September 2026

**The public-quote restriction that stood earlier this session is lifted.** A human-downloaded BAILII transcript (`Murphy-v-Sheffield-Hallam-EAT-6-99-1101.rtf`, saved from a browser session that could pass BAILII's Anubis bot-protection wall, which continues to block automated fetching) was obtained and placed in the prompts folder. Grok's prompt 170 findings quoted it; **this review independently extracted and read the RTF's own text directly — not just Grok's write-up of it — before accepting the correction.** All three previously-unverified facts are confirmed verbatim in the judgment text itself:

- **Award:** "They awarded him £2,500 compensation for that act of discrimination." (para 3)
- **Dates:** post advertised November 1997; applied 22 November 1997; invited to interview 16 December 1997; no interpreter arranged; adjourned to 18 December 1997. (paras 2–3)
- **Signer wording:** "The appellant appeared with Dr Sheppard, a highly competent amateur signer." (para 4) — this describes the *resumed* 18 December interview, not the 16 December no-show; no complaint was made about Dr Sheppard's competence, only that the appellant was not offered the job afterward.
- **Statute confirmed:** Disability Discrimination Act 1995, ss.5(2) and 6 for the 16 December interpreter failure (upheld, £2,500 awarded, respondent's cross-appeal on this point abandoned); s.5(1) causation question for the appointment/selection ground (appellant lost both at first instance and on this appeal).
- **Appointment ground dismissal, exact wording:** "The appellant failed to establish that his disability in fact played any part in his failure to be selected for the job. It was not an effective cause of the less favourable treatment. Hence his complaint in this respect failed. So too must this appeal. It is dismissed." (para 25)
- **Bench and citation:** HHJ Peter Clark, Lord Davies of Coity CBE, Mr A E R Manners. Hearing 7 December 1999, judgment delivered 11 January 2000. Appellant represented by Ms F Krause; respondent by Mr J N Galbraith-Marten of Dibb Lupton Alsop.

**Citation note — two valid suffix forms exist for this case, cite either but be consistent:** the RTF's own embedded document metadata carries `[1999] UKEAT 0006_19_0712 (07 December 1999)` — using the *hearing* date. Grok's prompt 170 findings and the swarb.co.uk title both use `[1999] UKEAT 0006_19_1101` / `[2000] EAT 6/99/1101` — using the *judgment-delivered* date (11 January 2000). Both point to the same case; this project's prior standing shorthand of **EAT/6/99** (the Appeal No. printed on the transcript itself) is the safest form to use in public copy, paired with either full citation.

**What this does NOT confirm or add:** the first-instance Employment Tribunal's full extended reasons (promulgated 11 November 1998, Sheffield, four days) were not retrieved — only the EAT's recitation of them. If a future draft wants detail beyond what the EAT judgment itself quotes (e.g. the tribunal's full reasoning at its own paragraph numbers, not the EAT's), that document is still outstanding.

**Updated public-copy line, now safe to use with the citation attached:**

> In *Murphy v Sheffield Hallam University* (EAT/6/99, [1999] UKEAT 0006_19_1101, 11 Jan 2000), an Employment Tribunal found a university had unlawfully discriminated against a profoundly deaf applicant under the Disability Discrimination Act 1995 by failing to arrange a sign language interpreter for his interview, awarding £2,500 compensation. The interview was adjourned and later completed with an interpreter present; the applicant's separate complaint that he was not offered the job because of his disability failed at both the tribunal and on appeal.

---

## Don't list (print near any applying-for-a-job/interview page)

Grok's own Don't list (in `Recruitment-prompts-103-108-claude-feedback.md`) is comprehensive and does not need to be re-typed here — read it in full before publishing anything. This independent pass adds one item, now resolved, and reinforces one:

- **Resolved (was "New"):** Murphy v Sheffield Hallam's £2,500 award, the December 1997 dates, and the "amateur signer" wording are now confirmed directly against the primary transcript (see RESOLVED section above) and may be quoted publicly with the EAT/6/99 citation attached. Do not omit the citation when quoting these figures — that is the one condition attached to lifting this restriction. Do not describe the "amateur signer" detail as a complaint about interpreter quality — the transcript is explicit that no such point was taken by the appellant.
- **Reinforced:** Do not print CSI as a transfer of the s.20 duty, and do not print a CSI hours cap in public copy — both hold after the live spot-check and remain exactly as contested as Grok flagged.

---

## What to do with this finding

| Scenario | Action |
|---|---|
| Someone asks "who pays for my interview interpreter?" | Two routes — employer/agency duty under the Equality Act, and separately AtW CSI (candidate-applied, 100% funded, apply before, paid after). Link GOV.UK CSI (spot-checked live, holds) + ACAS interviewing page. |
| Someone asks "do I have to tick disabled on the form?" | They can ask for a process adjustment without a general health disclosure. Link EHRC applicant s.60 guide + Elite Careplus as the enforcement example (not a Deaf case). |
| Someone wants to cite Murphy as precedent | Now fully citable — DDA 1995 (not Equality Act 2010), £2,500 awarded for the 16 Dec 1997 interpreter failure, appointment-discrimination claim separately failed. Use the public-copy line above, always with the EAT/6/99 citation attached. |
| Someone wants a letter/template | Use the existing template-batch tone (46–51). Ask booking/CSI/outcome questions per Grok's own scenario table. |
| Someone wants a new domain page | No. Stub under Welfare & Employment. |

---

## What actually closes the gap (ranked)

1. **FOI in the existing companion log** — Grok's five-question set (booker/payer identity; booking volumes and no-show counts; whether the process-adjustment question is held separately from health/monitoring questions; outsourced-recruitment contract terms) is well-designed and needs no changes. First wave: the six SWL boroughs + SWL ICB + named SWL trusts already logged, plus any in-house recruitment team those bodies use.
2. **Link the live resource** — GOV.UK CSI (re-confirmed live this pass); ACAS recruitment + interviewing pages; EHRC s.60 employer and applicant guides; EHRC Elite Careplus page; NDCS getting-a-job; BDF hearing-loss briefing for the 2–4 week lead time.
3. **A dated stub sentence** on an existing Welfare & Employment page — the lead sentence above, dated 14 September 2026 (this review), not 13 September (Grok's self-review date).
4. **A new draft** — only the two-routes card and the four-line invitation sentence, only after human sign-off. Murphy may now be referenced by name with its citation if either draft wants a concrete case example.

Additional item this pass: **before quoting a CSI-hours figure in anything public, open the live AtW staff-guide HTML section end-to-end** (still not done across two passes now — 104's original pass and this review). This is the one recurring "re-open before publish" item that keeps getting deferred; it should be the first thing done if this domain moves toward drafting.

---

## Per-prompt source register (keep; do not flatten)

| Prompt | Settled enough to link | Stays unpublished/contested | Do not promote |
|---|---|---|---|
| 103 gate | s.39 applicants; s.20 at recruitment; s.55 agencies; Sch. 8 knowledge; ACAS 30 Jun 2026 | No GB judgment on "cancelled because a full-time interpreter was assumed" | EEOC example as UK law |
| 104 money | CSI: candidate applies, 100%, before, paid after, 2-working-day decision (**spot-checked live 14 Sep 2026, holds verbatim**); BDF 2–4 week market; Murphy DDA 1995, £2,500 award, 16/18 Dec 1997 dates, "highly competent amateur signer" wording (**all fully verified against the primary EAT/6/99 transcript, 14 Sep 2026 — see RESOLVED section**) | CSI hours 2 vs 3 (still open after two passes); default private-sector booker unpublished | In-work AtW waits as CSI; 80% healthcare figure |
| 105 s.60 | Full exception list; only EHRC enforces the question; Elite Careplus 2021; CIPD forms labelled post-offer | Live ATS combined-box practice; EHRC s.60 report volumes | Elite Careplus as Deaf; "disabled tick-box always unlawful" |
| 106 international | Labelled international throughout | Historic Ontario OIS practice — confirm live | Any of it in a UK data cell |
| 107 lived | Murphy facts (**now fully verified, see RESOLVED section**); Limping Chicken 2 Oct 2024 mismatch; Rimmer para 221 for channel colour only | No DeafBlind employer-interview first-person; no national rate | Rimmer award; Clarke JCP; AtW-in-work quotes |
| 108 agency/ATS | s.55+s.56+s.109+s.110+s.111 stack; REC principle 4; Code 10.48 | Who books/pays when agency sits in the middle; named ATS config | Khan as interview case; "named board is in breach" |

---

## Cross-batch rules

Unchanged from Grok's self-review — confirmed still accurate on this pass:

- Distinct from 20–26/27–33 (benefits, Jobcentre — CSI is not a JCP appointment).
- Distinct from 52–54 (in-work AtW cap/clock — CSI has no cost-share and a 2-day decision aim).
- Distinct from 92–96 (OH starts after an offer; a pre-offer OH questionnaire is a s.60 problem, not OH).
- Distinct from 97–102 (in-post SLA assumes the job is already held).
- Distinct from 109–114 (grievance clock starts after the door is shut; this batch stops at the door).
- Distinct from 115–120 (DeafBlind in-post adjustments; recruitment-stage DeafBlind mention is thin here — Easy Read CSI naming a deafblind interpreter is the only hook).
- Shared facts not to reprint as new: AtW cap and 3,210 BSL-interpreter customers (20–26/52–54); Sch. 8/s.41 contract-worker split (97–99); Elite Careplus is the s.60 finding already used, not a new one.
- Held-back numbers: none inside 103–108. Prompt 170 (single-prompt Murphy verification patch) is now closed/resolved. Next free number on the live index is **171**.

---

**Adding a new batch after this review?** Confirm against `prompts/SuperGrok_Research_Prompt_Pack.md` NEXT PROMPT NUMBER line first. On 14 September 2026 that line is **171**.
