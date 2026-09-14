# Independent review — Prompt 164 (UK Deaf/DeafBlind travellers abroad)

Claude's independent check of Grok's findings for prompt 164. No separate Grok self-review file exists for this single prompt (consistent with how prompt 84 was handled) — this review stands in that slot.

**Date:** 14 September 2026
**File behind this:** `VRS-Telecoms-prompt-164-findings-uk-deaf-travellers-abroad.md`

---

## What I checked independently

I verified the two claims the whole prompt's "you cannot just use a foreign VRS" argument rests on:

- **Canada CAV User Agreement eligibility clause.** Confirmed **verbatim** by direct fetch of the PDF: "Only Canadian citizens or residents of Canada who (a) are Deaf, hard of hearing, or speech impaired, and (b) use American Sign Language and/or Langue des signes québécoise are eligible to register for the VRS Services." Grok quoted this exactly. Solid.

- **FCC SSN-waiver order (DA-15-589) and its treatment of foreign visitors.** Here I'd push back on Grok's framing, not the sourcing. Grok's finding says the waiver "does not delete the residence documentation condition" and lands on "Contested" / "Do not print 'UK visitors can register for US VRS.'" Reading the primary document directly, it's more permissive than that caution suggests: the order **explicitly names** "foreign students studying in the United States and residents of other countries who are visiting the United States or who have temporary visas for tourism, medical treatment, or other purposes" as the intended beneficiaries of the SSN waiver, and describes them registering with alternative ID (e.g. a passport) plus documentation of their presence in the US. That's the FCC naming tourists as an eligible category, not merely failing to exclude them.

  This doesn't flip the bottom line — a two-week leisure visitor still needs to find and assemble the right paperwork, a working VRS provider willing to process it, and it is genuinely unclear what "showing that such VRS consumers are residing in the United States" means for someone in a hotel rather than a lease — but Grok's caution undersells what the source says a little more than it oversells it, which is the less common failure mode in this project. Fair way to print it: *"US rules explicitly contemplate a foreign visitor registering for VRS with alternative ID in place of an SSN; whether a short leisure stay in practice satisfies the 'residing in the United States' documentation requirement is unresolved on the published text."* Don't print Grok's flatter "do not tell a UK visitor to just open Sorenson" line without that nuance — it's not wrong, but it reads more closed-off than the source actually is.

I did not re-verify the Australia NRS registration/address-document claim, the New Zealand overseas-FAQ wording, or the EENA 112 report-card figures (13 of 29 countries) — these are plausible, consistently sourced, and lower-stakes than the two US/Canada eligibility clauses the prompt's headline leans on hardest.

---

## Verdict for any public page

**Curate first, draft almost nothing — agree with the drafted headline, with the one correction above.** The finding is genuinely useful and easy to get wrong in exactly the direction this project worries about: a well-meaning "just use [Country]'s national VRS while you're there!" tip would be flatly false for three of the four systems (Canada's citizen/resident test, Australia's address-document test, and language mismatches — Auslan, ASL/LSQ, NZSL, none of which is BSL) and only conditionally true for the fourth (the US, where a visitor is at least a named eligible category, subject to unresolved practical friction).

Safe lead sentence:

> None of the national video relay services mapped for this project (US, Canada, Australia, New Zealand) is built for a UK BSL-signing visitor: three explicitly require citizenship, residency, or a matching local address, and all four operate in the destination country's own sign language, not BSL. The US is a partial exception — its rules name visiting foreigners as eligible to register — but the practical registration process for a short stay is unresolved.

### What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| What happens if you dial 999 BSL from abroad | Prompt 84 / Ofcom — connects to a UK control room only |
| What the destination country's own system actually is | Prompt 80 — do not re-derive |
| Inbound visitor-to-UK picture | Prompt 84 — the mirror finding |
| Official UK travel-health guidance | GOV.UK hospital-abroad page + FCDO English-interpreter-lists page — cite directly, don't paraphrase into something warmer than it is |

---

## Don't list (confirmed sound, one correction folded in)

Everything on the prompt's own don't-print instructions holds: don't tell a UK visitor to "just use" a foreign VRS; don't assume International Sign is accepted anywhere; don't print "GHIC includes a BSL interpreter"; don't conflate PRM/1107 mobility assistance with a language service; don't generalise the single RNID lived-experience account into a general claim. Add the one nuance above on the US FCC waiver — accurate but slightly oversold as a closed door in the current draft.

---

## What to do with this finding

| Scenario | Action |
|---|---|
| Someone asks "can I use the US/Canadian/Australian VRS on holiday?" | Canada: no (citizenship/residency test). Australia: no in practice (Auslan, address-document test). US: maybe, in principle, for a foreign visitor — but the practical registration path for a short stay is untested and shouldn't be promised. |
| Someone asks about calling 999 while on a trip abroad | 999 BSL will only ever reach a UK control room; it's useless for an emergency in the country they're actually in. |
| Someone wants a "what to do if you need medical care abroad" note | GHIC/EHIC is a charging mechanism, not a communication one; point to the official English-interpreter-list guidance and recommend checking travel insurance policy wording for interpreting cover specifically. |
| Someone has a UK BSL first-person account of a bad experience abroad | Worth collecting directly — this prompt found only one adjacent (non-BSL) UK travel account and confirmed the testimony gap is real, not a search failure. |

---

## What actually closes the gap (ranked)

1. **No further eligibility research needed on the four mapped countries** — the picture is clear enough to publish with the correction above.
2. **The lived-experience gap is the one item still open**, and this prompt correctly declined to manufacture testimony to fill it. If a genuine account surfaces later (a named UK BSL traveller who tried to register with a foreign VRS or use a foreign emergency number), that alone would justify a dedicated 165+ prompt — not before.
3. **A country-by-country EU 112 sign-language visitor-eligibility check** is the most answerable remaining question, per the prompt's own "what this does not close" list — a volunteer/FOI-shaped task, not a new Grok research prompt.

---

## Cross-batch rules

- Distinct from prompt 84 (inbound visitors to the UK) — this is the outbound mirror; don't conflate the two directions when citing either.
- Reuses prompt 80's country system descriptions and prompt 78's UK model rather than re-deriving them — correct discipline, no duplication found.
- **This closes the VRS-Telecoms domain's last open structural question.** The only unresolved item across 78–80, 84, 164 is the still-unissued dedicated lived-experience prompt, which 164 deliberately declined to force — leave it unissued rather than commissioning testimony-fishing.
