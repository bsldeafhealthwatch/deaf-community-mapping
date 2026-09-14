# Feedback for Claude — Household-Leave (independent review, after Grok 150–157, addenda 165–166)

Use this to decide what goes on any public workplace / carers page, what stays internal, and what becomes FOI. It is research constraint, not page copy. Do not paste Grok output onto the hub.

**Date:** 14 September 2026 (150–157 reviewed 14 Sep; addenda 165, 166 and 167 issued, run through Grok, and spot-checked same day; earnings-limit clarification added same day)
**Independent review by:** Claude, spot-checking Grok's own self-review (`Household-Leave-prompts-150-157-claude-feedback.md`) and Grok's answers to addenda 165, 166 and 167 against primary sources.
**Files behind this:**

- `Household-Leave-prompt-150-definitions-scope-stacking.md`
- `Household-Leave-prompt-151-evidence-negotiation-burden.md`
- `Household-Leave-prompt-152-stacking-interaction-effects.md`
- `Household-Leave-prompt-153-hra-article-8-reach.md`
- `Household-Leave-prompt-154-atw-welfare-funding-bridge.md`
- `Household-Leave-prompt-155-international-comparative.md`
- `Household-Leave-prompt-156-lived-experience-case-for-change.md`
- `Household-Leave-prompt-157-missed-milestone-workplace-cause.md`
- `Household-Leave-prompts-150-157-claude-feedback.md` (Grok's own self-review)
- `Household-Leave-prompt-165-age-continuity-past-16-18.md` (addendum — the dependant's age boundary)
- `Household-Leave-prompt-166-reciprocal-carers-allowance.md` (addendum — two partners each claiming Carer's Allowance for the other)
- `Household-Leave-prompt-167-parent-eol-employee-pip-findings.md` (addendum — emergency leave for a parent on DLA/PIP, the employee's own PIP, and bereavement leave)

Re-open before publish — GOV.UK carer's leave / dependants / parental leave / flexible-working / Carer's Allowance / Parental Bereavement Leave pages; ACAS Employment Rights Act 2025 page; Carer's Leave Regulations 2024 (**including reg. 7(4), see 167 below**); MAPLE 1999 Sch. 2 para. 7 and reg. 15 (**see corrections below**); ERA 1996 s.80J and s.57A (**s.57A(1)(c) and (3)–(5), see 165/167 below**); SSCBA 1992 s.70 (**see 166 below**); National Living Wage rate (**see earnings-limit clarification below**); ERA 2025 s.9 flexible-working reasonableness and its general bereavement-leave right (both 2027, not live); Carer's Allowance rate and earnings limit; *Qua v John Ford Morrison Solicitors* [2003] ICR 482 (**see 167 below**); *Make Work Pay* unpaid-carers consultation (closed 1 Sep 2026, response unpublished).

---

## Verdict

**Curate first. Draft almost nothing — Grok's own self-review already reaches this verdict and does the heavy lifting well.** This independent pass confirms the batch's central finding (household stacking is not a recognised category; four separate machines with four separate units of account) and the Article 8 correction (150/153), spot-checks load-bearing claims across the original batch and both addenda, and corrects **one factual error in prompt 150 / the self-review** that would matter if repeated in public copy.

> The four statutory rights exist separately. None of them treats "employee + disabled partner + EHCP child" as one qualifying situation. Planned appointments sit outside emergency dependants leave. Access to Work pays for the employee's own job, not for the household's care.

That sentence still stands as the one this batch is allowed to lead with. Three more sentences are now available to pair with it:

> Unpaid parental leave stops at the child's 18th birthday, disabled or not. Carer's leave and time off for dependants have no age limit written into the statute at all — an adult child who still reasonably relies on a parent is not excluded from either right on the face of the text, though no tribunal has ever tested that reading.

> Two partners who each care for the other can each claim Carer's Allowance — the statutory bar (SSCBA 1992 s.70) only stops two claims about the *same* cared-for person, not reciprocal claims about two different people. Each claim still has to independently clear the 35-hours and £204-earnings tests.

> The "35 hours" in Carer's Allowance is hours of *care given*, not hours of paid work. A 35-hour-a-week job does not itself disqualify a claim — but at anything close to the National Living Wage it will produce earnings well above the £204/week limit, which does disqualify it. It is the pay, not the hours worked, that trips the test.

> A parent's DLA or PIP award is not a key that unlocks or blocks the employee's own leave — carer's leave evidence cannot lawfully be made a condition of grant at all. There is no statutory bereavement-leave right in Great Britain for the death of a parent; the live hook after a death is s.57A's ordinary "reasonable time off" ground, not a separate bereavement product. Neither the employee's own PIP nor their spouse's support changes that employee's own eligibility — but a spouse who is also employed holds their own, separate leave pot in respect of the employee as *their* dependant.

### Correction: MAPLE Sch. 2 para. 7 already includes PIP — this is not a live ambiguity

Prompt 150 (and Grok's self-review, which repeats it in the "Verdict for any public page" table) states that the parental-leave whole-weeks exception "still names DLA, not PIP... EHCP" and flags this as **Contested**, framing it as an open question of whether the regulation has been updated. It has not been left open — it was settled over a decade ago.

The current in-force text of MAPLE 1999 Sch. 2 para. 7, fetched live from legislation.gov.uk on 14 September 2026, reads:

> "An employee may not take parental leave in a period other than the period which constitutes a week's leave for him under regulation 14 or a multiple of that period, except in a case where the child in respect of whom leave is taken is entitled to a disability living allowance, **armed forces independence payment or personal independence payment**."

The amendment footnotes on the same page date both insertions to **8 April 2013**: armed forces independence payment via SI 2013/591, and personal independence payment via SI 2013/388 reg. 2, Sch. para 22(5)(b). Both instruments amended the paragraph over twelve years before this batch was researched (11 September 2026).

This does not change the batch's core finding — an EHCP is still not the statutory key; PIP (or DLA, or AFIP) is. It also does not open a stacking route — the exception is about taking leave in periods shorter than a week, not about a bigger entitlement. But it should not be printed as "contested" or "not rewritten for PIP" — that line, if it reaches a public page, hands a reader (or a challenged employer) a wrong citation that is trivially checkable and already wrong on the face of the current statute. Correct prompt 150's table row and Grok's self-review table row to: "the exception covers DLA, AFIP, or PIP (added 2013) — not EHCP." **Addenda 165 and 166 both already carry this correction forward correctly.**

---

## Addendum 165 — age continuity past 16/18, spot-checked live

Raised as a genuine gap during review of 150–157: none of the original eight prompts tested what happens once a disabled dependant is chronologically an adult (16, 18, or older) but remains, in practice, as dependent on parental support as before — a common pattern given EHCPs can run to age 25.

**Headline, confirmed:** the toolkit splits at 18, and only for one of the four rights.

- **Unpaid parental leave** has a hard statutory cutoff. MAPLE 1999 reg. 15, fetched live: *"An employee may not exercise any entitlement to parental leave in respect of a child after the date of the child's 18th birthday."* Applies identically whether or not the child is disabled — the Sch. 2 para. 7 disabled-child exception only changes how leftover weeks may be taken (days rather than whole weeks), not how long the right lasts. **Verified live and holds verbatim.**
- **Carer's leave has no age ceiling.** ERA 1996 s.80J(2), fetched live, defines a dependant as a spouse/civil partner, **child**, or parent; someone living in the same household; or anyone who "reasonably relies on the employee to provide or arrange care." No age qualifier anywhere. **Verified live and holds verbatim.**
- **Time off for dependants (s.57A) has no age ceiling.** ERA 1996 s.57A(3)–(5), fetched live, defines "dependant" the same way, again with no age qualifier. **Verified live and holds verbatim.**

So for a disabled offspring who is chronologically 18+ but still reasonably relies on the employee: parental leave is definitely gone, but carer's leave and s.57A are not statutorily excluded — they were never age-gated to begin with. Grok's finding that "no named ET/EAT judgment applies either section to this exact fact pattern" is an absence finding, not a settled precedent.

**One thing to watch, not yet a correction:** prompt 165 states EHCP continuation "runs, in some cases, to the end of the academic year of the 25th birthday," citing Children and Families Act 2014 ss.45–46. That citation was **not independently re-verified this pass** — flag it as unconfirmed if it becomes load-bearing for a public claim.

---

## Addendum 166 — reciprocal Carer's Allowance between two partners, spot-checked live

Raised as a direct follow-on question: if a child is deliberately left out of the picture, and instead both partners are independently on PIP and each cares for the other 35+ hours a week, can they each claim Carer's Allowance for the other at the same time? 150 already established the *employment*-law side of this is symmetric and per-employee (carer's leave, s.57A, and flexible working don't care who's caring for whom, and don't stack because the caring runs both ways) — this addendum tests the narrower *benefits*-eligibility question, which 154 never touched.

**Headline, confirmed:** there is no statutory bar on reciprocal Carer's Allowance claims.

- **SSCBA 1992 s.70(7)** — fetched live from legislation.gov.uk: *"No person shall be entitled for the same day to—(a) more than one allowance under this section; or (b) both an allowance under this section and carer support payment."* This stops one person collecting two CAs. **Verified live and holds verbatim.**
- **SSCBA 1992 s.70(7ZA)** — fetched live: *"Where, apart from this subsection, two or more persons would have a relevant entitlement for the same day in respect of the same severely disabled person, one of them only shall have that entitlement..."* This stops two different people both being paid CA for caring for the **same** person. **Verified live and holds verbatim.**
- **Neither subsection addresses two different people caring for two different (each other) cared-for persons.** Confirmed directly against the legislation.gov.uk text this pass: both provisions are drafted around claims relating to the same cared-for person, and contain no language addressing reciprocal care between two different individuals. A claims CA because A cares for B; B claims CA because B cares for A — those are two different "severely disabled persons," so neither s.70(7) nor s.70(7ZA) applies, provided each partner claims only the one CA each.

Grok's finding is not a novel legal theory — it is a straightforward reading of the statute's own wording, and it holds. Carers UK's plain-English restatement ("If you care for someone who also cares for someone else however, you can both make a claim for Carer's Allowance if you meet the criteria") is consistent with this and was checked as advocacy restatement, not treated as a second source of law.

**Two supporting figures also re-verified live** against GOV.UK's Carer's Allowance eligibility page: the 35-hours-a-week care requirement, and the £204-a-week earnings limit — both confirmed as currently stated on the live page (page shows a 17 October 2024 update marker; the £204 figure and its 6 April 2026 effective date should still be cross-checked against the current benefit-rates publication if this is used close to the next uprating cycle).

**What genuinely remains a gap, not a finding either way:** no named Upper Tribunal decision or DWP Advice for Decision Making chapter walks through this exact two-partner-reciprocal-PIP pattern. The statute doesn't bar it, but nothing has tested it in practice either — the real-world constraint for most couples is likely to be the earnings cliff (both need to be under £204/week to qualify at all), not the reciprocal-claim structure itself.

**One knock-on effect worth keeping in public copy, per Grok's own finding:** if CA is actually paid in both directions, each partner typically loses any severe disability premium or equivalent extra amount on their own means-tested benefits, because that premium is usually withdrawn once someone else is being paid CA for caring for you. That is a real financial trade-off a household should know about before assuming "both can claim" is automatically the better outcome — it was not independently re-verified this pass (it rests on a Carers Support Centre toolkit and an Independent Age factsheet, not primary legislation) and should be flagged as sourced-but-not-primary if used publicly.

### Clarification — "35 hours" is care given, not hours worked; the earnings limit is what a 35-hour job actually trips

A natural follow-on question after 166: if the PIP-claiming partner also works a 35-hour-a-week job, does that block their Carer's Allowance claim? Checked directly against GOV.UK's Carer's Allowance eligibility page (already fetched live for 166): the 35-hour test is "You need to spend at least 35 hours a week **caring** for someone" — it is about care given, not paid employment. There is no rule in SSCBA 1992 s.70 or on GOV.UK's eligibility page that a 35-hour job is itself disqualifying, and no rule that caring hours and working hours cannot both independently reach 35 in the same week (exhausting as that combination would be in practice).

What actually disqualifies a 35-hour-a-week job in nearly every real case is the **"not gainfully employed" earnings test**, not the hours. The limit is £204/week net (after tax, National Insurance, and allowed deductions), a cliff-edge, not a taper. At the current National Living Wage of £12.71/hour (effective 1 April 2026 — [Bishop Fleming, 3 Mar 2026](https://www.bishopfleming.co.uk/insights/what-national-living-wage-april-2026); [Yerty minimum-wage guide](https://yerty.co.uk/guides/national-minimum-wage-2026)), a 35-hour week is £444.85 gross — well above £204/week even after tax and NI are deducted. So in practice a 35-hour contract at or near minimum wage does block the claim, but it is the pay clearing the earnings cliff that does it, not a rule against 35 hours of work as such. A much shorter working week, or a small amount of self-employed/irregular work kept deliberately under the limit, would not face the same block.

This distinction is worth keeping precise in public copy: "you can't work 35 hours and get Carer's Allowance" is not quite right and invites confusion with the unrelated 35-hours-of-care requirement. The accurate sentence is "your earnings from work, not your hours, are what's tested — and a full-time job at typical wages will almost always breach the £204 limit."

---

## Addendum 167 — emergency leave for a parent on DLA/PIP, the employee's own PIP, and bereavement leave, spot-checked live

Raised directly from a real anchor: an employee on a 35-hour contract, themselves on PIP and supported by a spouse, whose separate parent is on DLA/PIP and enters a terminal decline — all three Deaf. Five linked questions neither 150–157 nor 165/166 nor the EOL/palliative-care brief tested: does the parent's own benefit status gate the employee's leave; is there a statutory bereavement right for a parent's death; does s.57A's "reasonable" time have a practical ceiling under repeated terminal-decline crises; does SREL touch employment leave at all; and does the employee's *own* PIP, or a spouse's independent dependant right, change anything.

**Headline, confirmed:** none of the five questions produces a new statutory route — the toolkit is exactly as narrow here as 150 already found it to be elsewhere, but two of the five answers are genuinely useful correctives to have stated plainly.

- **Carer's Leave Regulations 2024 reg. 7(4)** — fetched live from legislation.gov.uk: *"An employer cannot require an employee to supply evidence in relation to a request [for carer's leave]."* **Verified live and holds verbatim.** This directly answers sub-question (1): a parent's DLA/PIP award is not an eligibility key for carer's leave, and — more usefully for a public page — an employer cannot lawfully make grant of carer's leave conditional on producing it. s.57A has no evidence subsection at all (only a duty under s.57A(2) to state the reason and likely length as soon as reasonably practicable) — confirmed by the same live fetch of s.57A.
- **ERA 1996 s.57A(1)** — fetched live, all five limbs confirmed verbatim, including **s.57A(1)(c): "in consequence of the death of a dependant."** This is the live statutory hook for time off *after* a parent's death. **Verified live and holds verbatim.**
- **Parental Bereavement Leave ("Jack's Law")** — fetched live from GOV.UK's eligibility page: eligibility turns on being "the child or baby's parent" (or their partner) at the time of a child's death or a stillbirth. Nothing in the eligibility test extends to the death of the employee's own parent. **Verified live: there is no statutory bereavement-leave right in Great Britain for the death of a parent** — the only live statutory hook is s.57A(1)(c)'s reasonable unpaid time off, not a separate bereavement-leave product. Grok's finding that ERA 2025's general unpaid bereavement right is not yet in force (targeted 2027) was not independently re-checked this pass but is consistent with the ERA 2025 s.9 flexible-working finding already verified for the main batch (also 2027, not live) — flag as unconfirmed if it becomes load-bearing on its own.

**Not independently re-verified this pass:** the *Qua v John Ford Morrison Solicitors* [2003] ICR 482 reading of "reasonable" and "unexpected" (that previous absences are relevant, and that a known recurring condition may mean a later episode is not "unexpected") — this is consistent with how *Qua* is already used elsewhere in this batch and in general ACAS commentary, but the specific sentence-level reading was not re-fetched from the judgment text this pass. Also not re-verified: the claim that SREL has no documented bearing on employment leave (an absence finding, inherently hard to verify beyond confirming SREL's own scope, which was already checked in the EOL/palliative-care brief) and the claim that a spouse's own s.57A/carer's-leave pot is available in respect of the employee as their dependant (this follows directly from s.57A(3)(a) and s.80J(2)(a), both already verified live for addendum 165 under near-identical wording, so it is treated as holding by direct extension rather than a fresh unconfirmed claim).

**What genuinely remains untested, flagged as such by Grok and not contradicted by this pass:** whether a spouse's s.57A or carer's-leave right extends to accompanying the employee to the *parent's* hospital bedside (rather than dealing with the employee's own emergency) is unpublished — no case or guidance answers it either way. Whether an employer's bare *request* (short of making it a condition of grant) for a parent's benefit letter is lawful is similarly unaddressed by any named source for s.57A, though reg. 7(4) settles the carer's-leave version of the question. **150's no-stacking finding is confirmed to hold on this triple-layered fact pattern too** — three Deaf, disabled household members does not create an extra statutory week or a combined pot; each of the employee's and spouse's rights remains a separate, per-employee machine.

---

## Claims re-verified live this pass

**Original batch (150–157):**

1. **Carer's Leave Regulations 2024 / GOV.UK cap sentence** — holds verbatim.
2. ***X v Y* [2004] EWCA Civ 662** — holds verbatim, fetched from the National Archives judgment text.

**Addendum 165:** MAPLE reg. 15 (parental leave's 18th-birthday cutoff), ERA 1996 s.80J (carer's leave dependant definition), and ERA 1996 s.57A(3)–(5) (time off for dependants definition) — all three verified live and hold verbatim.

**Addendum 166:** SSCBA 1992 s.70(7) and s.70(7ZA) — both verified live and hold verbatim, including the specific reading that neither bars reciprocal claims about two different cared-for persons. The 35-hours rule and £204 earnings limit on GOV.UK's eligibility page also confirmed live.

**Earnings-limit clarification:** current National Living Wage rate (£12.71/hour from 1 April 2026) checked via web search against multiple current sources; the £204/week limit itself was already verified live for 166.

**Addendum 167:** Carer's Leave Regulations 2024 reg. 7(4) (no evidence may be required before granting carer's leave), ERA 1996 s.57A(1) in full including the (1)(c) "death of a dependant" ground, and Parental Bereavement Leave's GOV.UK eligibility scope (child/stillbirth only, no parent ground) — all three verified live and hold verbatim.

The one claim that did **not** hold across any pass was the original MAPLE Sch. 2 para. 7 "DLA only" point — flagged as a correction, not a confirmation. The EHCP-to-25 citation in 165, the SDP-knock-on citation in 166, and the *Qua* "reasonable/unexpected" sentence-level reading, the SREL-has-no-bearing absence finding, and the spouse's-own-pot extension in 167 were **not** independently re-verified this pass (the last of these follows directly from already-verified s.57A(3)(a)/s.80J(2)(a) wording rather than resting on a fresh unconfirmed source) and are flagged as unconfirmed secondary points, not corrections.

---

## What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| Flexible working request | GOV.UK + ACAS Code. Day-one GB from 6 Apr 2024. Two requests / 12 months per *employee*. Two-month decision clock. ERA 2025 s.9 reasonableness test confirmed **not live** — 2027. |
| Time off for dependants | GOV.UK `/time-off-for-dependants` + ACAS. Per-incident, no annual cap, **no age cap on the dependant** (verified live). Planned hospital appointments are **out**. *Qua v John Ford Morrison* [2003] ICR 482. |
| Unpaid parental leave | GOV.UK + MAPLE 1999. 18 weeks *per child*. Day-one GB from 6 Apr 2026. **Hard cutoff at the child's 18th birthday** (reg. 15, verified live) — disabled or not. Default whole weeks unless the child gets DLA, AFIP, **or PIP** (corrected) — not EHCP. |
| Carer's leave | GOV.UK `/carers-leave` (cap sentence verified live) + ACAS. One week per employee per year. **Cannot** take a week per dependant. **No age cap on the dependant** (s.80J, verified live). Day-one from 6 Apr 2024. **Evidence cannot be required as a condition of grant** (reg. 7(4), verified live). |
| Carer's Allowance | GOV.UK `/carers-allowance/eligibility` (verified live). 35 hours/week **of care** (not of paid work), £204/week earnings limit (net, from work), £86.45 rate 2026/27. **No bar on reciprocal claims between two different people** (SSCBA 1992 s.70, verified live) — each claim independent. A 35-hour job is not itself barred — its likely earnings are what breach the limit. |
| Bereavement leave (a parent's death) | **No statutory bereavement-leave right exists in GB for the death of a parent** (verified live against Parental Bereavement Leave's GOV.UK eligibility page — child/stillbirth only). The live hook is s.57A(1)(c), ordinary reasonable-time-off, not a separate product. ERA 2025's general bereavement right is **not live** — 2027. |
| Article 8 | Point at *X v Y* (verified live) or print nothing. No named GB judgment whose ratio is Article 8 required any of these four rights. |
| Deaf employee's own workplace access | Existing AtW / AIS / Domain 14 pages. Do not caption them as household-leave funding. |

Thin original drafts worth doing *later*, after a human signs this file off:

1. A **one-screen right-chooser**: emergency → s.57A; planned disabled-child appointment with notice → carer's leave; longer block of childcare → parental leave (per child, ends at 18); pattern change → FW request. Four doors, four clocks, one week cap, one age wall (parental leave only).
2. A **four-line BSL process card**, only after a named employer's pack is opened.
3. A **watch**, not a page, on ERA 2025 s.9 commencement, the unpaid-carers consultation response, any named tribunal case testing s.57A/s.80J against an adult disabled dependant, and any UT/ADM decision testing reciprocal Carer's Allowance claims.

---

## Don't list (print near any household / carers / flexible-working / benefits page)

- Do not print that an employer's refusal, postponement, or process is unlawful, discriminatory, or an Article 8 breach without a named statute, regulation, or judgment.
- Do not print household-level stacking as a recognised category — 150's finding is that it is not.
- Do not invent an unofficial aggregate cap. 152 found a menu, not an aggregate.
- Do not treat an EHCP as a statutory key for carer's leave, s.57A, or the MAPLE whole-week exception. The exception is keyed to DLA, AFIP, or **PIP** — corrected; do not repeat "DLA only."
- Do not print that carer's leave or s.57A stop at 18 — verified live that neither states an age ceiling. Only parental leave has the 18th-birthday cutoff.
- Do not print that carer's leave or s.57A definitely *do* cover an adult disabled dependant as settled law — the statute text does not exclude it, but no tribunal has confirmed it either.
- Do not print that reciprocal Carer's Allowance claims are always paid, or that DWP bans them — SSCBA 1992 s.70 does not bar them (verified live), but each claim must independently clear the 35-hour and £204 tests.
- Do not print that PIP on the carer disqualifies them from claiming CA for someone else — not on the s.70 list (verified live).
- Do not print that "you can't work 35 hours and get Carer's Allowance" as a rule — the 35-hour test is care given, not paid work; it is the £204 earnings limit that a 35-hour job at typical wages breaches, not a bar on the hours themselves.
- Do not print the SDP-loss knock-on from 166 as independently verified primary law — it rests on secondary sources, flag as such.
- Do not print Article 8 as a free-standing ET claim against a private employer. *X v Y* [2004] EWCA Civ 662 (verified live).
- Do not recode *Dobson*, *Hedger*, *Thompson*, *Ghebrehiwt* as Article 8 authorities.
- Do not print that AtW covers household caring, or reprint the AtW cap/BSL-interpreter customer figures in this batch — those belong to 20–26 / 52–54 / 116.
- Do not print Carer's Allowance as an employment-retention product.
- Do not paste FMLA, EU 2019/1158, Irish 104 weeks, Norwegian/Swedish/Italian schemes into a UK cell (155) — international only.
- Do not paste Scotland's Carer Support Payment rival-carer rule (166) into an England cell.
- Do not print that a named employer caused a named missed family event without a source that says exactly that (157).
- Do not write ERA 2025 flexible-working reasonableness as live law — still 2027.
- Do not treat the EHCP-to-25 continuation detail (165) as independently verified — flag as unconfirmed if used publicly.
- Do not print that a parent's own DLA/PIP award is required, or usable as a gate, before an employee can take s.57A or carer's leave for them — neither right conditions eligibility on the dependant's benefit status, and carer's leave evidence cannot lawfully be demanded before granting it (reg. 7(4), verified live).
- Do not print that there is a statutory bereavement-leave right for the death of a parent in Great Britain — verified live that there is none; Jack's Law covers only a child's death or a stillbirth, and s.57A(1)(c)'s ordinary reasonable-time-off ground is the only live statutory hook after a parent's death.
- Do not print that a known, expected terminal decline automatically strips later crisis episodes of s.57A protection — no case holds that; *Qua* asks whether *that* occasion was unexpected on its own facts, not whether the general trajectory was foreseeable.
- Do not print that DWP's Special Rules for End of Life award changes, extends, or unlocks any employment-leave right — no documented join exists; SREL is a benefits fast-track for the patient, not an employment-law status.
- Do not print that a spouse is automatically entitled to accompany the employee to a *parent's* bedside under the spouse's own s.57A/carer's-leave right — that right exists for the employee as the spouse's own dependant, not as a second allocation for the parent, and whether it stretches to accompanying is unpublished (167).
- Do not wear a DEI or anti-DEI banner. Follow money and fulfilment — which clock, which cap, who pays.

---

## What to do with this finding

| Scenario | Action |
|---|---|
| "How much extra leave do we get because three of us are disabled?" | There is no extra pot. Point at the four live GOV.UK pages. Carer's leave is one week regardless of headcount. |
| "Our child is 19 and still needs us just as much — do we lose everything?" | Not automatically. Parental leave is gone at 18. Carer's leave and time off for dependants have no stated age limit — an open statutory reading, not a decided case. |
| "We're both disabled and each other's carer — can we both claim Carer's Allowance?" | Yes, on the statute's own text (verified live) — no bar on reciprocal claims for two different people. Each claim must independently clear 35 hours and the £204 earnings limit. Flag the possible loss of severe disability premium if both claims are paid. |
| "I'm on PIP and work a 35-hour contract — can I still get Carer's Allowance?" | The 35 hours of *work* is not itself the problem — the 35-hour *care* test is separate. The real block is almost certainly the £204/week earnings limit: a 35-hour job at or near the National Living Wage (£12.71/hr from April 2026 → ~£445 gross/week) will breach it. State it as an earnings problem, not an hours-of-work problem. |
| "My parent is on DLA/PIP and dying — can my employer demand proof of their benefit before letting me have time off?" | For carer's leave: no — evidence cannot lawfully be required as a condition of grant (reg. 7(4), verified live). For s.57A: the statute is silent on evidence; only a duty to explain the reason and likely length applies. The parent's benefit status is not an eligibility test either way. |
| "Is there paid or protected bereavement leave when a parent dies?" | No statutory bereavement-leave right exists for a parent's death in GB (verified live) — Jack's Law covers only a child's death or stillbirth. The live statutory hook is s.57A(1)(c)'s ordinary reasonable unpaid time off. Anything more is contractual or discretionary — check the employer's own policy. |
| "My parent's decline is expected — can my employer refuse time off for the next crisis because it's 'not unexpected' anymore?" | No case supports that reading. *Qua* asks whether *this* occasion was unexpected on its own facts and looks at the pattern of previous absences — it does not create a rule that a known terminal trajectory removes s.57A protection from every later episode. |
| "I'm on PIP myself and rely on my spouse — does that change my own leave rights, or my spouse's?" | Not the employee's own eligibility — no PIP-requester rule exists. But if the spouse is employed, they hold their own separate s.57A/carer's-leave entitlement in respect of the employee as *their* dependant — a genuinely separate pot, not a second allocation for the parent. Whether it stretches to accompanying the employee to the parent's bedside is untested. |
| Wants a letter / template | Use the ACAS model FW letter and the GOV.UK carer's-leave notice rule. Do not draft a "household stacking request" letter. |
| Wants a new domain page | No. One paragraph on an existing Welfare & Employment door, linking the live GOV.UK pages. |
| Wants to say Article 8 "protects" a private-sector carer | Point at *X v Y* (verified live) or print nothing. |
| Wants to say AtW should pay for the child's EHCP review | Point at 154 — different system; AtW will not. |
| Cites the parental-leave "disabled child" exception | State it correctly: DLA, AFIP, or PIP — not EHCP. |

---

## What actually closes the gap (ranked)

1. **Link the live statute pages** — GOV.UK carer's leave, dependants, parental leave (correct DLA/PIP citation, note 18th-birthday cutoff), flexible working, Carer's Allowance eligibility (note no reciprocal-claim bar, and the care-hours vs. work-hours distinction). That is enough for a public door.
2. **Watch, do not FOI-invent a series** — ERA 2025 s.9 commencement; the unpublished *Make Work Pay* consultation response; any tribunal case on s.57A/s.80J and an adult disabled dependant; any UT/ADM decision on reciprocal CA.
3. **One optional FOI, only if a human wants a policy-history cell** — whether the 2023 Act impact assessment or the 2026 unpaid-carers review considered a per-dependant week or the 18th-birthday cutoff for disabled children. Yes/no-or-document.
4. **Do not FOI employers** for stacked-request refusal counts.
5. **A dated stub sentence** on an existing working-carers page: "Access to Work is for the employee's own job. Carer's Allowance is a separate benefit with an earnings limit — not an hours-of-work limit. Neither is extra statutory leave. Parental leave ends at 18; carer's leave and time off for dependants have no stated age limit. Two partners who each care for the other can each claim Carer's Allowance, subject to the usual hours-of-care and earnings tests. A parent's own DLA/PIP is not a gate on your leave, and carer's-leave evidence can never be demanded before it's granted. There is no statutory bereavement leave for a parent's death — only the ordinary time-off-for-dependants right applies."
6. **A new draft** — only the one-screen chooser, after sign-off.

---

## Cross-batch rules

- Distinct from **144/145** (EAP service design), **72–77** (CODA), **34–37/EOL** (patient access — including the EOL/palliative-care brief, which covers the *patient's* NHS/hospice/DWP access, not the working relative's leave rights), **20–26/52–54/116** (AtW is the employee's own support), **109–114** (grievance ladder), **66–71** (the employee as the person ageing).
- Shared facts not to reprint as new discoveries here: AtW cap and BSL-interpreter customer figures; NRCPD headcount; ONS sandwich-carer/Contact figures; Carer's Allowance rate; civil-servant AtW exclusion.
- **Numbering correction to the self-review.** Grok's own feedback file for 150–157 closed with "Next free number at this review date is 164" — stale by the time it was checked; 165, 166 and 167 were each issued correctly at the then-current next-free number, cross-checked live against the index each time. The index header now reads **"NEXT PROMPT NUMBER TO USE: 168."**
- Radar, not a new prompt: ERA 2025 s.9 and its general bereavement-leave right (both 2027); unpaid-carers consultation response; MAPLE PIP/DLA/AFIP citation now corrected; a tribunal case on s.57A/s.80J and an adult disabled dependant; a UT/ADM decision on reciprocal Carer's Allowance; any case testing a spouse's s.57A/carer's-leave right to accompany the employee to a third party's (e.g. parent's) crisis.

---

## Nice to add (not a new prompt)

Editorial only — none of these has a live trigger as of 14 September 2026. Each is logged with its trigger and ready-to-paste wording.

| # | What | Trigger (not yet met) | Ready-to-paste wording |
|---|---|---|---|
| 1 | Pair Carers UK's cap sentence with GOV.UK's planned-appointment exclusion | A working-carers / household-leave hub page gets built (none exists yet) | Carers UK: *"If you need to care for more than one person, you cannot take a week of carer's leave for each dependant — you can only take one week every 12 months."* GOV.UK: *"You cannot have time off if you knew about a situation beforehand. For example you would not be covered if you wanted to take your child to hospital for an appointment. You might get parental leave instead."* |
| 2 | Patch 156's "live ask" row with the consultation outcome | The *Make Work Pay* unpaid-carers consultation publishes its response — **unpublished** | Not yet actionable. |
| 3 | Dated addendum for a first-person account of the exact join | Such testimony surfaces — **none found** | Not yet actionable. |
| 4 | Add a "no age cap" line next to the parental-leave 18th-birthday note | Hub page built (same trigger as #1) | GOV.UK carer's leave and dependants pages do not state an age limit for the dependant (verified live). |
| 5 | Add a "reciprocal claims allowed" line to any Carer's Allowance summary | Hub page built (same trigger as #1) | "Two people who each care for the other can each claim Carer's Allowance if they meet the criteria — the rule against two claims only applies where both are claiming for the *same* person. Each claim still needs its own 35 hours of care a week and earnings at or under £204 a week." |
| 6 | Add a "care hours ≠ work hours" line to any Carer's Allowance summary | Hub page built (same trigger as #1) | "The 35-hour test is about hours spent caring, not hours worked in a job. A full-time job doesn't automatically block a claim — but its earnings almost always will, since the limit is £204 a week net and a full-time job at typical wages pays well above that." |

**Batch 150–157 can close, with prompt 150's MAPLE/PIP row corrected before anything public repeats it. Addenda 165, 166 and 167 can also close** — all core statutory citations across the three (MAPLE reg. 15; ERA 1996 s.80J and s.57A, including s.57A(1)(c) and (3)–(5); SSCBA 1992 s.70(7) and (7ZA); the 35-hours and £204 figures; Carer's Leave Regulations 2024 reg. 7(4); Parental Bereavement Leave's child/stillbirth-only eligibility scope) were independently verified live and hold verbatim. Several secondary citations remain unconfirmed and should be flagged if they become load-bearing: 165's EHCP-to-25 detail (CFA 2014 ss.45–46), 166's severe-disability-premium knock-on (Carers Support Centre / Independent Age, not primary legislation), and 167's *Qua* sentence-level reading, SREL-has-no-bearing absence finding, and spouse's-own-pot extension (the last of these follows directly from already-verified statutory wording rather than resting on a fresh unconfirmed source). Policy-gap, not rights-violation. Next free prompt number is **168** (verified live against the master index this pass).
