# Feedback for Claude — Interpreter Regulation & Agencies (independent review, after Grok 81–83)

Independent Claude review. Grok's own self-review (`Interpreter-Regulation-prompts-81-83-claude-feedback.md`) is a separate, prior document — this file does not restate it, and where the two disagree that is flagged explicitly. Use this to decide what goes on any public "book an interpreter / NRCPD" page, what stays internal, and what becomes FOI. It is research constraint, not page copy.

**Date:** 13 September 2026
**Files behind this:**

- `prompts/Interpreter-Regulation-prompt-81-nrcpd-rbsli-regulatory-status.md`
- `prompts/Interpreter-Regulation-prompt-82-agency-procurement-model.md`
- `prompts/Interpreter-Regulation-prompt-83-workforce-sufficiency-reform.md`
- `prompts/Interpreter-Regulation-prompts-81-83-claude-feedback.md` (Grok's own review, read alongside this one, not duplicated)
- Prompt text: `prompts/Interpreter-Regulation-prompts-81-83.md`

Re-open before publish — `nrcpd.org.uk/registration-figures`, the AIS 1.32 long-read, and RM6302 Lot 4 buyer docs all move.

This batch is the regulator / agency / workforce layer sitting underneath AIS 34–37, Templates 46–51, AtW 52–54, the EOL/palliative brief's RIDB figures, and VRS 78–80. It must not re-cost SWL GP spend, and it must not be treated as having settled the lived-experience question — that leg was deliberately held back (see Cross-batch rules).

**Proposed domain:** Interpreter Regulation & Agencies is already on the dashboard. Do not stand up a new domain off this batch.

---

## Spot-check performed on this pass

Two load-bearing claims were checked against the live primary source rather than trusted from the quote, since the entire batch verdict rests on them:

1. **NRCPD registration-figures table** (`nrcpd.org.uk/registration-figures`, fetched 13 September 2026). Confirms: Sign Language Interpreter **1,664** (exact match to Grok's 10 September pass); Deafblind Interpreter **19**, with East Midlands, South West, and Yorkshire and The Humber all showing no registrants; the page's own dual-registration caveat verbatim ("The total includes dual registrations (ie one person on more than one register)"). Minor drift on other categories (Trainee SLI 242 vs Grok's 241, Translator 97 vs 96, Relay Intralingual 63 vs 62) — a one-point live-counter movement across the three days between scrapes, not a sourcing error. **Verdict: the RIDB-zero claim and the SLI 1,664 headline both hold.**
2. **NRCPD statutory-regulation page** (`nrcpd.org.uk/statutory-regulation`, fetched 13 September 2026). Confirms verbatim: NRCPD currently holds "voluntary Registers"; statutory regulation "will make it illegal for someone who isn't registered to practise"; this is a "long term aim" and NRCPD states "we are not going to set a timescale for achieving it" and does "not know how long it will take, or even if we will achieve it." **Verdict: the voluntary-not-statutory distinction, and the "no criminal offence" conclusion built on it, both hold.** This is the gate claim the whole batch depends on — it survives the check.

No other cells were independently re-verified on this pass. The agency-procurement chain (82) and the workforce/reform findings (83) rest on named primary documents (AIS implementation guidance, NHS Standard Contract SC12.3, PHSO releases, CCS RM6302, NUBSLI fee guidance, *Locked Out*, ASLI/Wales correspondence) that were not re-fetched here; their sourcing looks sound on inspection (title, publisher, date, URL all present) but "looks sound on inspection" is not the same standard as the two claims above.

---

## Verdict for any public page

**Curate first. Draft almost nothing.**

The one sentence a page is allowed to lead with:

> NRCPD and RBSLI are voluntary registers, not statutory regulators. NHS and other public contracts choose to require them (AIS 1.32 is the live NHS hook). There is no UK statute that makes unregistered BSL interpreting a criminal offence. On 13 September 2026 the NRCPD public table showed 19 Registered Interpreters for Deafblind People nationally, with none listed in the East Midlands, South West, or Yorkshire and The Humber.

What already exists and should be linked, not rewritten:

| Need | Point at |
|---|---|
| Check a named professional is registered | NRCPD "Check the register" / "Find a professional." RBSLI name search. SRLPDC if the booking is Scotland-based. |
| What registration is supposed to mean | NRCPD Registration page (approved course, Code, complaints, CPD, DBS, insurance) — the body's own promise, not an audit. |
| Complain about a named registrant | NRCPD concerns page + March 2026 Professional Conduct Complaints Procedure v1.3. RBSLI complaints page if that register applies. |
| Complain that nobody came / family was used | Trust PALS → PHSO. Two named upheld cases (Alan Graham, UHB, Feb 2026; Samantha, GP, Aug 2026) both hold the provider, not the agency. Templates 46–51. |
| Book for an NHS appointment | The trust/ICB/GP's contracted agency (SWL: DAL + Sign Solutions VRI; SEL: DA Languages + InterpretersLive, three boroughs only) — not a national NRCPD switchboard. |
| Freelancer rate expectation | NUBSLI April 2026 medians (London RSLI full day £375). Label as a union median, not an NHS tariff. |

Thin original drafts worth doing later, after a human signs this file off:

1. A one-screen "voluntary register, contract requirement" box — that distinction is the whole of prompt 81's finding.
2. A four-line "confirm the interpreter's NRCPD/RBSLI number before the appointment" line for a GP/hospital letter template. Never "illegal if unregistered."
3. A complaint-routing chooser: person → NRCPD/RBSLI; missed booking → PALS/PHSO; agency desk itself → the commissioner's contract manager (Wales SOP states this split explicitly; England's is inferred from AIS 1.32 + specification wording).
4. A dated RIDB strip: 19 live, three English regions at zero, £15k grant targeting 68 — labelled as target, not delivered headcount.

---

## Scenario → action table

| Scenario | Action |
|---|---|
| Someone asks "is my interpreter properly regulated?" | Point to the register check tools. Say plainly: registration is voluntary, not a licence to practise — a name on the list is a quality signal and a complaints route, not proof of a legal requirement being met. |
| Someone wants a letter/template asking for an NRCPD-registered interpreter | Fine — this is what AIS 1.32 already supports. Do not add "or it's illegal" to the letter. |
| Someone's interpreter didn't show up | Route to PALS then PHSO if unresolved, per the two published upheld cases. Do not route them to NRCPD unless they are complaining about a named individual's conduct. |
| Someone wants to complain that "the agency never sent anyone" | Explain the chain (organisation → agency → registrant/VRI/unfilled) and that no published case has yet made the agency itself the respondent — the provider remains liable regardless. This is an honest gap, not a dead end: PALS/PHSO is still the route, and the provider can (and should) be told the failure was the agency's. |
| Someone proposes a new domain page or "AIS Compliance Monitor" tool off this batch | Decline. This batch documents the regulatory/procurement *architecture*; it is not a live compliance-scoring dataset, and Grok's own review already flagged this exact overreach risk (see the DAGM 42 precedent it cites). |
| Someone wants to cite "68 RIDB" or an "official interpreter ratio" | Don't. See Don't list. |

---

## Don't list (print near any interpreter / NRCPD page)

- Do not write "using an unregistered interpreter is illegal." It is not a criminal offence under any UK statute found on this pass.
- Do not write "NRCPD is the statutory regulator." It is a charity/company (charity 1170904 England & Wales, SC051776 Scotland) holding voluntary registers. Statutory regulation is its own stated long-term aim with no published timetable — confirmed verbatim on spot-check.
- Do not write "there are now 68 RIDB." GOV.UK's 23 June 2026 grant announcement *targets* 68 against a historic baseline of 8. The live table checked on 13 September 2026 still shows **19**.
- Do not add NRCPD category totals together to produce a unique-person headcount — the table's own caveat says duals are included. Use the homepage live feed (2,087 on Grok's 10 September pass; not independently re-checked here) when a single total is needed, and date it.
- Do not reprint RBSLI "52" from a 2019 academic paper as a current figure. No 2025–26 RBSLI headcount was found by either Grok or this review.
- Do not write "Ofqual licenses BSL interpreters." Ofqual regulates Signature as an awarding organisation and the INTRA6 qualification (RQF 603/5484/7). Registration with NRCPD is a separate, second gate after the qualification.
- Do not collapse the new BSL GCSE (an Ofqual-regulated school qualification, rules announced 13 November 2025) with interpreter registration — different products, different purposes.
- Do not write that the AIS/Equality Act duty "transfers" to the agency when a booking fails. SC12.3 binds the NHS Provider; the Equality Act binds the service the patient is trying to use. Both published PHSO findings (UHB, GP practice) held the provider, not the agency.
- Do not print RM6302 Lot 4 unit rates or invent a CCS BSL hourly rate — Framework Schedule 3 is not public.
- Do not recycle the DAL ~37% company-wide gross margin figure as a BSL-booking-specific haircut.
- Do not print *Locked Out*'s "92% fulfilment KPI" as an official CCS figure — it is the Board's description, not confirmed on the public CCS page. Keep it labelled Contested.
- Do not print an official interpreter-to-Deaf-population ratio. None exists. ONS 2021 main-language E&W is 22,000; *Locked Out*/BDA's 87,000 and 151,000 are different denominators measuring different things. Any ratio arithmetic (e.g. "~15 main-language users per SLI cell") is researcher-derived, not a published standard, and belongs in a footnote at most.
- Do not print "20.6% accept healthcare work / 7.65% accept mental health work" as if it were NRCPD administrative data — it is *Locked Out*'s own Board-cited percentage, footnoted to its own evidence pack, not re-opened by Grok or by this review.
- Do not claim England has a funded general-RSLI workforce plan. The only named growth funding found is the £15,000 RIDB competency-assessment grant — nothing equivalent exists for the general Sign Language Interpreter register.
- Do not import NHS England clinical-staffing agency price caps as a BSL interpreting tariff — different regime entirely.
- Do not hold any page built from this batch out as a regulator, a booking desk, or legal advice.
- Do not wear a DEI or anti-DEI banner. Follow money and fulfilment: headcount, hours, who pays, who was actually held liable.

---

## Where this review differs from Grok's own self-review

Grok's self-review is thorough and largely holds up — its Don't list, its confidence table, and its "hand Claude these files in this order" note are all sound and this review does not repeat them wholesale. Three points worth flagging rather than silently endorsing:

1. **Grok's self-review references files this project has not confirmed exist under those names in the Claude project** (`VRS-Telecoms-prompts-78-80-claude-feedback.md`, `VRS-Telecoms-prompt-84-international-visitors-uk.md`). The master index confirms the VRS/Telecoms domain (78–80, 84, 164) was independently reviewed and closed 14 September 2026 — after Grok's 10 September self-review was written. Treat Grok's cross-references to that domain as pointing at material that has since moved/been superseded by the closed-domain reviews already on file (`claude/grok-findings-vrs-telecoms.md`), not as an open dependency.
2. **Grok's self-review says interpreter-regulation lived experience is "deferred to prompt 85."** The master index instead records that prompt 84 went to VRS-Telecoms and states a lived-experience leg for *this* batch, if wanted, needs a fresh number from **164+** (now effectively **165+**, since 164 has since been issued and closed under VRS-Telecoms). Grok's "85" appears to be a stale placeholder from before the numbering settled. **Do not issue 85 for this purpose** — see Cross-batch rules below and the index update accompanying this review.
3. **The spot-check in this review is narrower than Grok's own scope** — two gate claims only, not a full re-verification of 82's procurement chain or 83's workforce reform claims. Those remain Grok-sourced and un-independently-verified beyond "the citation looks properly formed." Flag this to a human before anything from 82 or 83 goes on a public page; the AIS 1.32 / SC12.3 architecture (already independently verified in the AIS 34–37 review) is the one piece of 82 this review treats as solid by inheritance.

---

## What actually closes the gap (ranked)

1. **Fold into the existing FOI companion log** — do not build a dedicated interpreter-regulation FOI wave. At most add: (a) named SWL/SEL trusts + ICB already on the tracker — last FY BSL bookings requested/fulfilled/cancelled by supplier, F2F vs VRI split, unit rate if held; (b) NRCPD, via right of reply before FOI — unique-person count by category/nation at a stated date, complaints received/closed/sanctions 2023–25; (c) CCS or one ICB — whether a BSL-specific fulfilment KPI exists in RM6302 Lot 4 or a local call-off, and what percentage.
2. **Link the live resources** — NRCPD/RBSLI/SRLPDC register-check tools, NRCPD's concerns/complaints page, PALS/PHSO escalation path. None of this needs drafting; it needs linking with a publish date on the snapshot figures.
3. **A dated stub sentence** on the existing Interpreter Regulation & Agencies dashboard entry, updated with the 13 September 2026 spot-check figures, superseding the 10 September figures where they've moved.
4. **A new draft** — only the four thin items listed under "Thin original drafts" above, and only after a human signs off this file. Nothing else.

---

## Cross-batch rules

- Distinct from AIS 34–37 (the legal *duty* to provide communication support) and Templates 46–51 (the letters that invoke that duty) — this batch is the regulator/agency/workforce layer underneath both. Do not re-derive AIS wording or template text from this batch; cross-check against it instead.
- Distinct from VRS-Telecoms 78–80/84/164 (relay technology and travel), which is a fully closed, separately reviewed domain as of 14 September 2026. Do not reopen it here or treat this batch as extending it.
- Distinct from the EOL/palliative-care brief's RIDB figures — this batch generalises that domain-specific finding to the general interpreter register; the EOL brief's own RIDB snapshot (5 September 2026: 19/68) is superseded for citation purposes by this batch's 10 September Grok pass and this review's 13 September spot-check, all of which agree the live figure is still 19.
- Shared facts that must not be reprinted as if this batch discovered them: AIS 1.32's wording and the NHS Standard Contract SC12.3 clause were already sourced in the AIS 34–37 review; this batch applies them to the agency layer, it does not re-source them.
- **Held-back prompt numbers and why they stay held:** this batch's fourth leg — lived experience / the case for statutory regulation versus better purchaser enforcement — was deliberately not issued as prompt 84 in this batch (84 went to VRS-Telecoms' international-visitors prompt instead). **It was never issued at all** — not as 84, and Grok's own self-review's reference to "85" does not match the master index, which reserves the next free number as 165+ (with 164 now used and closed). **If this lived-experience leg is picked up later, it must be issued fresh from 165+, not 85.** This review's accompanying index update flags that explicitly so the gap is not silently filled by a stray earlier placeholder number.
