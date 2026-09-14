# Feedback for Claude — Templates section (after Grok 46–51)

Use this to update `claude/templates-section-ideas.md`. It is research constraint, not letter copy. Do not paste Grok output into a live template.

**Date:** 9 September 2026  
**Files behind this:** `AIS-prompt-46` … `AIS-prompt-51` in the artifacts folder.

---

## Verdict for the section

**Curate first. Draft almost nothing.**

SignHealth already owns the “put my needs on the record” letter (2025, BSL + HoH + deafblind variants, BSL explainer video). Disability Justice already owns complaint + letter-before-action generators. RNID has a hand-in card. Citizens Advice / Patients Association cover generic process.

The only clean holes worth a *thin* original draft later:

1. **Confirm an in-person registered interpreter for a named date** (not VRI).
2. **Today’s interpreter did not arrive — rebook and confirm.**

Do not draft those until a human has signed off 46–51. Do not draft an LBA. Do not clone SignHealth.

---

## Paste into the ideas-doc “Don’t” list (from 49)

- Do not name a nurse/doctor as the villain. Name the practice, clinic or trust.
- Do not write “illegal,” “non-compliant with the Act,” “fraud,” “misconduct.”
- Do not put “letter before action,” costs, or “we will sue” on a first request.
- Do not invent deadlines (25 working days is local policy, not the 2009 Regulations).
- Do not say AIS bans VRI. 2025 guidance: offer F2F *or* remote for routine care; remote is “not a total replacement.”
- Do not hold the site out as a law firm or the letter out as legal advice.
- Do not invite extra publication (press, Facebook, staff personal email).
- Do not ask for another person’s health details or a child’s name without a consent warning.
- Do not ship written legal English only and call it the grassroots layer.

---

## Disclaimer to print next to every letter (CA model)

> This is a sample letter for **England**. It is general information, not legal advice and not complaints advocacy. Check every fact before you send it. Name the GP practice, clinic or trust — not a member of staff unless you need the name to identify the appointment. Do not copy this letter to social media or the press. If you are writing for someone else, attach their written consent. If you want to take legal action, get a solicitor or Law Centre. Free NHS complaints advocacy: ask your local Healthwatch, or search “NHS complaints advocacy” + your area (VoiceAbility 0300 303 1660 is one provider, not every area).

---

## Page structure Claude should use

1. **Chooser, not a dump**  
   What do you need to do?  
   - Record my communication needs → **link SignHealth** (do not rewrite).  
   - Confirm an interpreter for a date that is still in the future → hole B (PALS / booking desk).  
   - The interpreter did not come today → hole C.  
   - Something already went wrong → link RNID how-to + Disability Justice generator + NHS.uk complaints page.  
   - I am an advocate writing for someone else → consent first (PHSO form / 48).

2. **England badge** on every letter. Scotland has a tighter F2F-default policy — do not paste it into an English letter.

3. **Two channels on anything original** (51): short boxed English (reading age ~9–11) + BSL video “what this letter says / how to send it.” Easy Read-for-learning-disability is a cousin, not a substitute. Commission a registered **Sign Language Translator** (NRCPD), not an LLM, for the BSL twin.

4. **Deafblind is its own download**, not a footnote. SignHealth already splits this.

---

## Routing cheat-sheet (50) — put beside the chooser

| Need | Write to |
|---|---|
| Appointment still in the future | Clinic booking team. If they stall: **PALS**. Not a formal complaint yet. |
| GP record / GP complaint | **Practice manager** |
| Past hospital / trust failure | Trust complaints **or** ICB — **not both** |
| Interpreter no-show today | Reception now + PALS email the same day |
| Agency late / rude | The **NHS body that booked them** |

**Contested, so do not hard-code:** NHS.uk still says primary-care complaints go to NHS England; Age UK Dec 2025 and Patients Association send them to the ICB. UI text: “Check your ICB complaints page and the NHS.uk how-to-complain page on the day you send.”

---

## Voice rules (48)

| Who is writing | Voice | Deadline language | LBA line |
|---|---|---|---|
| Patient | “I” | Confirm before [appointment date] | No |
| Advocate | “On behalf of” + attached consent; reply to the advocate | Same | No on first ask |
| Solicitor | Out of scope for this site | 14 days only when a claim is real | Separate product, after complaint |

---

## Links to curate (live as of Sep 2026 — re-check before publish)

- SignHealth needs letter: https://signhealth.org.uk/with-deaf-people/campaigns/still-sick-of-it/communication-needs-template-letter/  
  Note on the page: they still say **DCB 1605**; current name is **DAPB1605**. One-line caption, do not silently “correct” their PDF.
- SignHealth BSL explainer of that letter: https://www.youtube.com/watch?v=-Xw5nnTd4SY
- RNID comms card: https://rnid.org.uk/wp-content/uploads/2022/11/health-and-care-comms-card.pdf
- RNID rights / how to complain: https://rnid.org.uk/information-and-support/your-rights/access-to-health-and-social-care/
- Disability Justice generators: https://www.disabilityjustice.org.uk/take-action/accessible-information-and-communication/
- NHS.uk how to complain: https://www.nhs.uk/using-the-nhs/about-the-nhs/how-to-complain-to-the-nhs/
- AIS 2025 implementation guidance (F2F vs remote paragraph): https://www.england.nhs.uk/long-read/accessible-information-standard-implementation-guidance/
- Find an ICB: https://www.nhs.uk/nhs-services/find-your-local-integrated-care-board
- VoiceAbility NHS complaints advocacy: https://www.voiceability.org/about-advocacy/types-of-advocacy/nhs-complaints-advocacy

---

## Nice-to-haves (only if the section is built)

Not required to start. Do not let these become a build.

- **Static “who to write to” lookup** that hits NHS.uk / trust PALS pages rather than a homemade address book (addresses rot).
- **Consent attachment** download (PHSO already has the official form — link it).
- **Same-day no-show email** even shorter than a letter: 6 lines, boxes only.
- **DeafBlind booking line** that names RIDB / deafblind manual / communicator-guide as *asks*, not as a claim that AIS mandates a specific professional title.
- **Nation toggle** later (Scotland / Wales / NI). England-only at v1.
- **“What happened after I sent it”** log sheet (VoiceAbility already uses a timeline). Link, don’t rebuild.
- Caption on SignHealth: current standard code is DAPB1605 v4.0 (approved 3 Jun 2025).

---

## Out of scope for Claude

- Auto-filling letters from an NHS login.
- A chatbot that “decides” if VRI was lawful.
- Scoring a named trust as “non-compliant with the Act” from a template tool (that is the DAGM product, and prompt 42 already forbids volunteer legal conclusions).
- Hosting users’ filled letters.
- Updating the SuperGrok master index from this note — that file is not in this artifacts folder.

---

## Suggested one-paragraph status for the ideas doc

> Grok 46–51 (9 Sep 2026): legal basis, existing letters, professional vs personal, don’t-list, routing, BSL-first. Section should be a **chooser that links SignHealth / RNID / Disability Justice / NHS.uk**. Original drafting limited to a dated F2F booking request and a same-day no-show note, both in boxed plain English plus a commissioned BSL explainer, both with the CA-style disclaimer. No LBA. No staff-naming. No “VRI is illegal.” Review every line against 46–51 before anything goes live.
