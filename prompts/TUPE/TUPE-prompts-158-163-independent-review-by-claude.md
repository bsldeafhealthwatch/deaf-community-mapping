# Feedback for Claude — TUPE (after Grok 158–163)

Use this to decide what goes on any public page, what stays internal, and what becomes FOI. It is research constraint, not page copy. Do not paste Grok output onto a public page, into a template letter, or into the live dossier.

**Date:** 14 September 2026 (independent review originally dated 13 September 2026; browser-confirmed refresh same day — the underlying legal analysis is unchanged)
**Files behind this:**

- `TUPE-prompt-158-legal-basis-adjustment-transfer-eli.md`
- `TUPE-prompt-159-information-consultation-accessibility.md`
- `TUPE-prompt-160-atw-interpreter-kit-continuity-gap.md`
- `TUPE-prompt-161-passport-eli-due-diligence.md`
- `TUPE-prompt-162-international-comparative.md`
- `TUPE-prompt-163-lived-experience-case-for-change.md`
- Prior independent review: `TUPE-prompts-158-163-independent-review-by-claude.md` (13 Sep 2026) and `claude/grok-findings-tupe.md` (project, same date)
- Grok's own self-review: `TUPE-prompts-158-163-claude-feedback.md`

**Re-open before publish** — the AtW employer factsheet (7 Oct 2025) and staff guide, the ACAS TUPE transfer-plan checklists and after-transfer page, NHS Employers Health Passport pages, the Civil Service exporting-manager page, and the Unite handbook. The staff guide in particular moves without a changelog entry against this heading (see below) — re-fetch again the week any stub goes up.

This batch is the legal-employer-change event: what happens to an already-agreed reasonable adjustment when a Deaf/BSL/DeafBlind employee's actual employer changes under TUPE. Do not collapse it into prompt 102 (passport travel inside one employer), 121–126 (stable employer, outsourced channel), 109–114 (post-transfer grievance ladder — downstream, read alongside, not duplicated), or 134–140 (devices/kit in a stable job).

**Proposed domain:** stub under the existing Welfare & Employment cluster, alongside 92–157. Not a new numbered Domain.

---

## Spot-check result (browser-confirmed 14 September 2026)

Two load-bearing claims were checked live rather than trusted from the findings files, per this project's sourced-and-dated standard. An earlier automated pass this same day could not surface the second claim via WebFetch and flagged it as unconfirmed, pending a human opening the live page directly — that has now been done, and the result below supersedes the automated pass.

1. **AtW employer factsheet ("cannot automatically transfer awards for support workers or travel")** — **re-verified verbatim.** The live GOV.UK factsheet page returns the identical sentence: *"they may be able to transfer equipment to their new employer, but they cannot automatically transfer awards for support workers or travel"* and the same "contact the Access to Work team" instruction, with the same 7 October 2025 update date the findings file cites. TUPE is not named on this page. This half of the pair holds.

2. **AtW staff guide TUPE block ("New employer (new owner of business), same job" / "should be treated as a repeat application" / "obliged to take on… cost sharing agreements with AtW")** — **browser-confirmed live and still present, 14 September 2026.** A human opened the published staff-guide URL directly and searched the page text. The block is still in the Change of circumstances chapter, paragraphs 39–44, verbatim: *"Under the TUPE regulations, the new owner of a business is obliged to take on the contractual obligations of their predecessor. This includes the cost sharing agreements with AtW."* Trigger language is still "If a customer makes contact…"; the case-manager instructions to update details, contact the new employer to confirm carry-forward, and flag equipment ownership/maintenance obligations are unchanged. The renegotiate-the-support-worker language is still there at paragraphs 41–44. Immediately after it, a second, distinct box — *"New employer, different business, same job"* (paragraphs 45–49, "some elements will not be transferable") — covers the more common private-sector service-provision-change / lost-retender pattern; which box case managers actually apply to an SPC is unpublished. The cost-share "job movers" bullet is also still live: takeover + same job = repeat application; takeover + fundamental duty change = new application with a new start date.

   **What was actually stale was not the block — it was the landing date we had been citing.** The page shows a visible "Updated 18 June 2026," a JSON-LD `dateModified` of 18 June 2026 10:50, and a separate `govuk:updated-at` meta stamp of 4 September 2026 10:37 — three different timestamps on the same page, none of which is 13 November 2025. That date should not be re-cited as current anywhere. The TUPE hyperlink embedded on the page still points at a dead Directgov URL; do not treat that link as a live GOV.UK TUPE explainer in its own right.

   The earlier automated-fetch pass this same day returned a mismatched update date and a table of contents with no visible "TUPE" heading, and treated that as inconclusive rather than as proof of removal — correctly, as it turned out: the tool was very likely truncating a long, deeply nested government page before reaching the relevant sub-block, not reporting a page that had actually changed. The lesson generalises: an automated fetch failing to surface a specific block on a page like this one is evidence of nothing on its own, in either direction, until a human confirms by direct search.

**How to describe the pair now, if anything goes public:** not "two DWP texts disagree" as if one contradicted the other, and not "the staff-guide block was removed." They address different audiences, and the staff guide itself already splits takeover-of-the-business/same-job from different-business/same-job. The factsheet never mentions TUPE. Both still require someone to phone AtW. Neither is an automatic system event.

Everything else in the prior review's legal analysis (TUPE reg.4/11/12, the Equality Act s.20 knowledge defence, *Gunn*, the ELI closed list) rests on legislation.gov.uk statutory text, which does not carry the same live-drift risk as a DWP operational guidance page, and is not re-litigated here.

---

## Verdict for any public page

**Curate first. Draft almost nothing.** Unchanged from the 13 September review.

The one sentence a page is allowed to lead with: *"TUPE transfers your contract automatically, and the new employer owes you the Equality Act duty to make reasonable adjustments from day one — but there is no published rule that your specific interpreter booking, passport, or Access to Work award transfers with you automatically, and DWP's own public guidance to employers and its internal guidance to case managers do not say the same thing."* Both halves are now browser-confirmed live as of 14 September 2026 — safe to print as written, dated to this review. Re-fetch before any future public use; this page moves without a changelog entry against this heading.

That single administrative mismatch — not a discovered legal breach, not a collected personal story — is what this batch actually proved. No UK tribunal has decided whether an informal or passport-recorded adjustment is a TUPE contractual term (158). No named case exists of a Deaf/BSL/DeafBlind employee's TUPE consultation running without access (159). No documented case exists of a booking lapsing specifically because of a TUPE transfer (160). No due-diligence template beyond one union training handbook even lists "reasonable adjustments accommodated" as a thing to ask about (161). No first-person UK testimony of this exact event exists at all (163). Every one of those absences is a finding to log, not a gap to fill with a plausible-sounding page.

### What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| What TUPE is, in plain terms | ACAS TUPE hub (`acas.org.uk/tupe`) |
| "What happens to my adjustments after I transfer" | ACAS *After a transfer* page — "The new employer must make sure they have put in place any reasonable adjustments for disabled employees." |
| Keeping a record so a new manager (or employer) knows what's agreed | ACAS reasonable-adjustments record page / TUC-GMB model passport / NHS Employers Health Passport if NHS — all intra-employer products, not TUPE-specific |
| "Will my Access to Work award continue?" | DWP's two pages side by side — factsheet ("cannot automatically transfer... contact the Access to Work team," re-verified live) and staff-guide TUPE block ("should be treated as a repeat application," **browser-confirmed live 14 Sep 2026, paras 39–44 — do not cite 13 Nov 2025 as its current date**) |
| Accessible consultation | EHRC's hybrid-working meeting-access guidance (names a BSL interpreter as an example) — general meeting-access guidance, not TUPE-specific |
| What happens if it goes wrong after the transfer | The existing Grievance & Escalation material (109–114) |

### Thin original drafts worth doing later, after a human signs this file off

1. A **"two documents, two audiences" callout** — juxtaposing the AtW factsheet sentence and the AtW staff-guide sentence, both now confirmed live. Lowest-risk output of this batch.
2. A **short "questions to ask before your TUPE date" list** for a Deaf/BSL/DeafBlind employee — framed as questions to ask, not guaranteed rights.
3. A **template email to a prospective new employer** — needs sign-off; must not imply a legal entitlement to a reply or continuity that 158/160/161 all found unpublished.

---

## Don't list (print near any public page)

- Do not print "TUPE requires the adjustment to transfer" — regulation 4 does not name disability, reasonable adjustments, passports, or Access to Work.
- Do not print "employee liability information must include disability status / adjustments / a passport" — regulation 11 is a closed list and none of its heads names it.
- Do not print a silent or incomplete ELI pack as an Equality Act breach against the employee — regulation 12 is a compensation claim between the outgoing and incoming employer, not an employee remedy.
- Do not print any "grace period" for the incoming employer's Equality Act duty — none exists; the duty bites from the moment the contract has effect, subject to the Schedule 8 paragraph 20 knowledge defence.
- Do not print that a named employer's TUPE consultation, ELI disclosure, or due-diligence process was unlawful without a named statute, regulation, or judgment.
- Do not treat English captions, a written pack, or "the union will explain it" as discharging a documented BSL-interpreter request for the consultation meeting.
- Do not print "Access to Work continues automatically across TUPE" **or** "Access to Work always requires a brand-new application after TUPE" — both are false on the texts as found, now that both texts are confirmed live.
- Do not print "the two DWP texts disagree" as if one contradicted the other — they address different audiences, and the staff guide splits takeover-of-business from different-business itself.
- Do not print that the staff-guide TUPE block was withdrawn, moved, or removed. It was not — only the landing date previously cited (13 November 2025) was stale; the page's actual timestamps are 18 June 2026 (visible/JSON-LD) and 4 September 2026 (`govuk:updated-at` meta).
- Do not treat the TUPE hyperlink embedded on the staff-guide page as a live GOV.UK TUPE explainer — it points at a dead Directgov URL.
- Do not print a workplace adjustment passport as a legal guarantee that the incoming employer must implement the old list without a fresh reasonableness assessment.
- Do not paste Northern Ireland's 14-day ELI clock into a GB claim (GB is 28 days), and do not paste COSOP or Civil Service inter-departmental guidance into a private-sector TUPE claim.
- Do not cite *Gunn*, *Stinton v Cambria Automobiles*, or *Anne v GOSH* as authority that an informal adjustment or passport transfers under TUPE — none of the three decides that question.
- Do not fill any UK cell with EU, US, Australian, or Canadian material from prompt 162 — label it international, context only.
- Do not invent or generalise a first-person "the interpreter vanished on TUPE day" account — none was found anywhere searched. That absence is the finding for prompt 163.
- Do not reuse the batch's banned names (Bussey, Clinton, Graham, Rimmer, Clarke, Borys, Murphy, Bentley, Davies, Fletcher, Iqbal, Khan, or Lisa's 2016 blog) as TUPE-transfer accounts.

### Key citations kept for reference (legal/procedural batch — do not compress further)

| Prompt | Load-bearing source | Value | Confidence |
|---|---|---|---|
| 158 | TUPE 2006 reg.4 (legislation.gov.uk) | Transfers "rights, powers, duties and liabilities under or in connection with" the contract; disability/RA/passport not named | Verified as live GB statutory text |
| 158 | TUPE 2006 reg.11 (legislation.gov.uk) | Closed ELI list; disability/adjustments/passport absent | Verified |
| 158 | *NHS Direct NHS Trust v Gunn* UKEAT/0128/14/BA (14 May 2015) | Transferring employee is not an EqA "applicant" for the existing job; does not decide informal-adjustment transfer | Verified as closest join, not a holding on adjustments |
| 158 | Equality Act 2010 Sch.8 para.20 | Knowledge defence — no s.20 duty without actual/constructive knowledge; no published grace period | Verified |
| 159 | ACAS *How to inform and consult* | "Disabled employees who might need reasonable adjustments – for example documents in an accessible format" — names documents, not BSL | Verified (not re-fetched this pass) |
| 159 | TUPE 2006 reg.13/13A | Representatives-first duty; direct consultation only where no reps and small enough | Verified as statutory text |
| 160 | DWP *Access to Work factsheet for employers* | Support-worker/travel awards "cannot automatically transfer"; contact AtW | **Re-verified live 14 Sep 2026, verbatim match** |
| 160 | DWP *Access to Work: staff guide*, TUPE block | Same-job takeover "should be treated as a repeat application" | **Browser-confirmed live 14 Sep 2026, paras 39–44, verbatim. Not withdrawn. Do not re-cite 13 Nov 2025 as current — page timestamps are 18 Jun 2026 / 4 Sep 2026.** |
| 161 | Unite *Handling TUPE Transfers* v3 | Only published template listing "details of any reasonable adjustments that have been accommodated" as extra due-diligence | Verified as closest artefact found (not re-fetched this pass) |
| 162 | Directive 2001/23/EC; BGB §613a; US successor-liability line | Every jurisdiction repeats the same split between transfer-of-contract and accommodation-by-current-employer | International pattern; not a UK finding |
| 163 | Scope *Keeping disability equipment when you leave your job* | "In most cases, this support will end with your employment" — resignation language, not TUPE same-job | Verified as adjacent, not this object |

---

## What to do with this finding

| Scenario | Action |
|---|---|
| Someone asks "does my interpreter booking transfer under TUPE?" | No settled answer — point to the factsheet/staff-guide pair (160, both confirmed live) and the Equality Act's day-one duty (158). Describe them as two audiences, not a disagreement. |
| Someone wants a letter or template | Not yet — needs human sign-off, since no source guarantees a right to reply or continuity |
| Someone wants a new domain page | No — a stub under Welfare & Employment, cross-linked from AtW, Passports (102), and Outsourced Services (121–126) material |
| Someone asks for a number (how often adjustments lapse on TUPE) | None exists — say so plainly |

---

## What actually closes the gap (ranked)

1. **Re-fetch the AtW staff guide the week any stub goes up.** Confirmed live and unchanged as of 14 September 2026 (browser-verified), but the page has now shown three different timestamps across two review passes in one day without a changelog entry against this specific heading — treat it as a page that moves silently and re-check on a short cycle before any public use, not as settled indefinitely.
2. **FOI to DWP** (existing companion log): how often is the staff-guide's carry-forward script actually used by case managers, versus customers being told to submit a fresh application in practice. Also worth asking: which box (same-business-takeover vs different-business-same-job) case managers actually apply to a service-provision change / lost retender, since the guide itself leaves that unpublished.
3. **A direct, low-cost ask to ACAS and CIPD** for the contents of their TUPE due-diligence checklists (paywalled/download-gated content, not withheld — just unopened).
4. **Link the two existing live DWP pages side by side** rather than drafting new summary copy — both are now confirmed live and safe to quote as written.
5. **A new draft** (the pre-transfer checklist, the employer email template) — only after 1–4, and only with human sign-off.

---

## Cross-batch rules

- Distinct from 102 (intra-employer/Civil-Service-move passport friction) — this batch is the legal-employer-change event itself.
- Distinct from 121–126 (stable employer, outsourced channel) — here the employer's legal identity changes.
- Distinct from 109–114 (Grievance & Escalation) — downstream, read alongside, do not duplicate.
- Distinct from 134–140 (Devices & Technology) — kit and captions in a stable job, not a change of employer.
- Prompt 162's international material fills no UK cell; keep it labelled international if referenced at all.
- No held-back legs — the lived-experience prompt (163) ran as part of the batch and returned a confirmed absence.
- Next free number: confirm against the live master index before issuing anything new (162 is the last number formally closed in this batch; the index's own "next free" line takes precedence over any figure carried in this file).
