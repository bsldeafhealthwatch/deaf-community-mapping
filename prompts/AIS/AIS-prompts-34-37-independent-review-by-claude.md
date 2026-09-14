# Feedback for Claude — AIS (after Grok 34–37)

Use this to decide what goes on any public page, what stays internal, and what becomes FOI. It is research constraint, not page copy. Do not paste Grok output onto a public page, into a template letter, or into the live dossier.

**Date:** 13 September 2026
**Files behind this:**

- `AIS-prompt-34-legal-status-scope-enforcement.md`
- `AIS-prompt-35-data-findings-flag-failures.md`
- `AIS-prompt-36-comparative-international-good-practice.md`
- `AIS-prompt-37-lived-experience-case-for-change.md`

Re-open before publish — the DAPB1605 v4.0 assurance end date (30 June 2027), the RADF national compliance checklist date (30 September 2026) and the DAPB4019 conformance dates (health 31 March 2027 / social care 31 October 2027), the NHS Standard Contract year (2026/27 SC12.3 cited here — a new contract year lands every April), and CQC's "AIS is not assured by CQC" guidance page (last updated 10 March 2026 at the time of this pass). All of these are dated commitments or annually-refreshed documents that this batch's whole legal-status argument leans on.

This batch is the **gate** for AIS work in this project — it establishes what the Standard actually requires before any patient-facing material gets built on top of it. The Templates section (46–51) already did exactly that: it drafted the actual letter guidance using this batch's legal findings as its foundation, and its own review (`grok-findings-templates-section.md`) is where the drafting decisions live. **Do not re-derive template wording from this file** — point to the Templates review instead. This batch's job is narrower: is AIS legally binding, does it require in-person BSL, how often does it fail in practice, what does elsewhere do better, and what has it actually cost real people. Distinct from the EOL/palliative brief (`claude/deaf-deafblind-eol-palliative-care-brief.md`), which applies AIS to a specific care setting rather than examining the Standard itself.

**Proposed domain:** none needed — this is the legal and evidentiary foundation for the existing "NHS Interpreter Provision & BSL Health Access" domain (21 figures, the largest domain on the dashboard). Most of that domain's figures likely already trace back to this batch's sources (*Still Ignored*, *Locked Out*); this review is the point to confirm that rather than re-sourcing the domain from scratch.

---

## Verdict for any public page

**Curate first. Most of the drafting is already done in the Templates review — this batch supplies the legal spine, not new copy.**

The one sentence a page is allowed to lead with: *"AIS is now a 'must comply' information standard, not a discretionary one — but it does not require an in-person BSL interpreter for a planned, non-emergency appointment; it only says the person should be offered the choice, and no national data exists on how often that choice is actually offered."*

That is the load-bearing finding across all four prompts: AIS looks stronger on paper since July 2025 than it is in practice, and the gap between "must comply" and "nobody has published a compliance rate" is the real story, not a discovered illegality.

### What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| Legal basis for a communication-needs request or complaint | Templates section prompt 46 (`grok-findings-templates-section.md`) — already built directly on this batch |
| An actual letter template | Templates section prompts 47–51 — SignHealth's needs-notification letter, Disability Justice's complaint/LBA generator, RNID's hand-in card are already identified as the ones to link, not duplicate |
| National failure-rate figures for citation elsewhere in the dossier | *Still Ignored* (SignHealth/RNID, 2025) and *Locked Out* (BSL Advisory Board, GOV.UK, 27 Nov 2025) — both already cited here and should be the single source of truth wherever this project quotes an AIS failure statistic |
| A good-practice example | Royal Trinity Hospice's 2025 access-and-inclusion programme (contact-method half only — flashing doorbell, email-first contact, BSL Talk & Tour) |
| Scotland's tighter rule, for comparison only | Public Health Scotland's *Interpreting, Communication Support and Translation National Policy* — clearly labelled Scotland, never pasted into an England claim |

### Thin original drafts worth doing later, after a human signs this file off

1. A **one-paragraph "what AIS actually requires" explainer** distinguishing the three legal layers (the s.250/s.95 information-standard duty, NHS Standard Contract SC12.3, and the Equality Act/CQC/Care Act layer underneath) — useful because most advocacy material collapses these into one undifferentiated "the law says," and this batch is the only place that keeps them apart.
2. A **short RADF/AIS disambiguation note** — these are two related but separate standards with two different compliance timelines, and conflating them is an easy, recurring mistake this batch specifically warns against.

---

## Don't list (print near any public page)

- Do not say AIS requires an in-person BSL interpreter for every planned appointment. The 2025 implementation guidance says remote interpretation "is not a total replacement" and that for routine care the patient "should be given the option of remote or face-to-face" — that is patient choice, not a mandated default.
- Do not say video relay/VRI use for a planned appointment is a breach of AIS or unlawful. No numbered AIS requirement says this; it is, at most, a departure from guidance, and usually an Equality Act question rather than an AIS one.
- Do not say section 95 of the Health and Care Act 2022 "has not been enacted." It was commenced on 7 July 2025 by SI 2025/807. The accurate claim is that the "must comply" duty is now in force, but the monitoring, waiver, and penalty machinery that would make it feel enforced has not been used publicly against named NHS bodies — *Locked Out* (November 2025) still describes an enforcement vacuum, and that description remains operationally fair even though the underlying statute has changed.
- Do not conflate the Accessible Information Standard (DAPB1605) with the Reasonable Adjustment Digital Flag (DAPB4019). They are related but separate standards with separate compliance deadlines — RADF's national checklist target is 30 September 2026; DAPB4019 conformance dates are health 31 March 2027 and social care 31 October 2027. Both being live does not mean either is actually stopping a patient being telephoned.
- Do not cite the University Hospitals Birmingham £8,000 fixed-penalty case (Mr X, November 2022) as an "AIS enforcement" example. CQC issued that under Regulation 11 (consent), not as an AIS-named finding, and CQC has explicitly said it does not assure AIS — that responsibility sits with commissioners.
- Do not quote SignHealth's 2014 *Sick of It* figures (cardiovascular/mental-health outcome disparities) as if they were 2025 AIS-compliance rates. *Still Ignored* (2025) is the current access-process data; *Sick of It* is an older, different kind of finding.
- Do not inflate the *Still Ignored* VRS-preference sub-sample (n = 37: 24% agree VRS is suitable in place of in-person, 54% disagree) into a national preference poll — it is explicitly a small sub-sample.
- Do not present the Healthwatch phone-call testimony (Healthwatch England, Devon/Plymouth/Torbay, Sandwell) as named or formally investigated cases — they are anonymised or aggregated community feedback, not PHSO findings, and should always be labelled as such.
- Do not claim any missed-appointment (DNA) rate improved because of a sticky flag or a face-to-face-default policy anywhere in the world. No peer-reviewed before/after study was found; any such claim is MODELLED at best and should be labelled that way if used at all.
- Do not paste Scotland's national interpreting policy (face-to-face as the preferred and main method) into an England-facing claim as if it were the English rule — it is real, it is tighter than AIS, and it is Scotland-only.
- Do not treat South West London ICB's December 2024 reasonable-adjustments flag rollout as a proven fix — Healthwatch Kingston notes the rollout happened; nobody has independently evaluated whether it actually stopped the phone-call pattern.

---

## What to do with this finding

| Scenario | Action |
|---|---|
| Someone asks "is my hospital legally required to book me an in-person interpreter?" | No bright-line AIS answer — point to the Equality Act's stronger anticipatory-adjustment duty once the patient has stated an in-person need, and to the Templates section's letter guidance for how to phrase that request |
| Someone wants a statistic for a talk or page about NHS interpreter failures | Use *Still Ignored* / *Locked Out* directly rather than an older or smaller-sample figure from this batch — check whether the dossier's existing NHS domain figures already trace to these two sources before adding a duplicate |
| Someone wants to know if a specific trust breached the law | This batch does not support that conclusion for any named trust beyond the handful of cases already publicly adjudicated (Alan Graham/UHB, Mr X/UHB, Samantha, Mrs E) — do not extend those findings to any other trust |
| Someone wants a new domain page on AIS itself | Not needed — the existing NHS Interpreter Provision & BSL Health Access domain is the right home; this batch is its legal foundation |

---

## What actually closes the gap (ranked)

1. **Confirm the existing NHS domain's figures against this batch's sources** — the dossier's 21-figure NHS domain almost certainly already draws on *Still Ignored* and *Locked Out*; this review is the moment to check those figures are cited correctly (right report, right year, right sample size) rather than commissioning new research.
2. **An FOI or direct ask to South West London ICB** asking whether the December 2024 reasonable-adjustments flag rollout has been evaluated, and if so with what result — this is the one live, local, answerable question this batch surfaces that nobody has chased yet.
3. **Write the Scotland-policy sentence and the ADA "primary consideration" standard into a short comparative note** for anyone drafting future AIS advocacy asks — both are ranked in prompt 36 as the most transferable improvements, ahead of anything requiring new legislation.
4. **A new draft** — only the two thin items above (the three-layer explainer, the RADF/AIS disambiguation note), and only after a human signs off, since both risk being over-simplified into exactly the kind of collapsed "the law says" claim this batch warns against.

---

## Cross-batch rules

- Distinct from Templates 46–51 — that batch is the drafting layer built on top of this one; do not re-derive letter wording here.
- Distinct from the EOL/palliative brief — that applies AIS to end-of-life care specifically; this batch examines the Standard in general.
- Shared facts that must not be reprinted as if this batch discovered them: the RIDB/interpreter-workforce figures live in Interpreter Regulation (81–83), not here; the SWL BSL request volume (878, Oct 2024–Jun 2025) is a pre-existing project figure, not a finding of this batch.
- No held-back prompt numbers — all four prompts in this batch (34–37) were run and are captured above.
