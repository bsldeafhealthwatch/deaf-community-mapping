# Independent review — VRS & Telecoms Equity (prompts 78–80, 84)

This is Claude's independent check of Grok's findings, separate from Grok's own self-review file (`VRS-Telecoms-prompts-78-80-claude-feedback.md`, in this folder). Use this to decide what's safe to publish; it does not replace re-opening a live source before anything goes on a public page.

**Date:** 13 September 2026 (78–80); updated 13 September 2026 for prompt 84 findings.
**Files behind this:**

- `VRS-Telecoms-prompt-78-per-org-contract-third-party-refusal.md`
- `VRS-Telecoms-prompt-79-home-office-travel-gap.md`
- `VRS-Telecoms-prompt-80-international-comparators.md`
- `VRS-Telecoms-prompt-84-findings-international-visitors-uk.md`

**Batch status: fully run.** All four prompts in this domain now have findings. The lived-experience leg was never issued a number and still needs one from 164+ if run later (see below) — that is the only genuinely open item left in this domain.

---

## Part 1 — Prompts 78–80 (per-org VRS model, home/office/travel gap, international comparators)

### What I checked independently

I spot-checked two of the load-bearing claims the whole batch's legal argument rests on, since this batch had no prior sourcing pass to check against:

- **Ofcom's 2019 EECC consultation** (cited as the document where Ofcom declined to mandate non-emergency video relay, footnoted "para 10.25"). The document exists at the cited URL and carries the cited publication date (17 December 2019) — confirmed via search. I was not able to re-open the PDF itself to re-quote paragraph 10.25 word-for-word (fetch blocked); treat the paragraph number as unverified until someone opens the live document, but the document's existence and date are solid.
- **Contact Scotland BSL's supplier change to Sign Solutions on 1 December 2025.** Independently confirmed via a third-party source (Generations Working Together, 25 Nov 2025 notice) describing the same transition date ("1 minute past midnight, 1 December 2025") and the same incoming supplier. This is a genuinely fast-moving fact and it checks out.

I did not re-verify every row in the findings tables (there are over 70 sourced rows across three files). The rows most worth re-opening before publish are the ones Grok itself already flagged as **Contested** or with an hours caveat (BA's VRS hours, Jet2's "24/7" claim, the Contact Scotland 2025 work/international exclusion) — see Grok's own gap table, which is accurate and doesn't need duplicating here.

### Verdict for any public page

**Agree with Grok's own verdict: curate first, draft almost nothing.** This batch's genuine finding is an absence, not a scandal — there is no UK judgment, no penetration-rate statistic, and no national non-emergency VRS duty for England and Wales — and an absence is easy to overstate into a false "X is illegal" claim if drafted loosely. The one sentence safe to lead a page with:

> In England and Wales a Deaf BSL user cannot pick up a phone and dial any UK number the way a hearing person can. The commercial product is a directory of organisations that have bought a listing. 999 BSL (emergencies) and Contact Scotland BSL (Scotland-resident users) are the two public exceptions.

### What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| Emergency BSL calling | 999 BSL app / `999bsl.co.uk` |
| Everyday any-number VRS (Scotland residents only) | Contact Scotland BSL, Sign Solutions from 1 Dec 2025 |
| A named organisation that has bought VRS | That organisation's own page → its named supplier's directory |
| Workplace VRS funding | Access to Work (prompts 52–54) — do not duplicate the cap/wait figures here, cross-link |
| Text to any UK number today | Relay UK — label it text, never BSL |
| The full airline/airport travel picture | Grok's own addendum table in `VRS-Telecoms-prompts-78-80-claude-feedback.md` — thorough and dated; no need to redo it |

---

## Part 2 — Prompt 84 (inbound international Deaf/DeafBlind visitors)

### What I checked independently

Two load-bearing claims underpin the whole prompt's argument that inbound provision is "BSL-shaped" and excludes ASL/International Sign — I verified both directly against the primary source rather than trusting the quote:

- **Ofcom, emergency video relay consumer page:** "If 999BSL interpreters are familiar with Irish Sign Language, they are free to use it if this benefits a deaf caller in an emergency situation" — with no mandate, and no equivalent sentence for ASL or International Sign. **Confirmed verbatim** by direct fetch of the live page. Grok's characterisation (ISL is discretionary, not required; ASL/International Sign unaddressed) is accurate.
- **NHS England AIS requirements (DAPB1605):** "The provision of a language other than English interpretation or translation is out of scope of this standard." **Confirmed verbatim** by direct fetch. Requirement 1.32's interpreter-qualification wording (NRCPD/RBSLI registration, DBS, code of conduct) was also confirmed verbatim on the same page.

Both of prompt 84's central legal claims — Ofcom has not required non-BSL sign languages on 999 BSL, and AIS itself excludes non-disability-related language interpretation from scope — are solid. This is the load-bearing logic for the prompt's most quotable and most easily misused line ("a visitor whose language is ASL/ISL/LSF/DGS/International Sign has no published UK public VRS product"), so it was worth checking directly rather than taking on trust.

I did not independently re-verify the airport/police/airline rows (Heathrow Convo QR, Manchester SignLive, force-by-force 101 listings, Ryanair's BSL+ISL directory rows) — these are the kind of live, frequently-changing supplier facts that need re-opening at publish time regardless of how carefully they were sourced now, and Grok's own "re-open before any public travel strip" list at the end of the file already names the right ones.

Note also: the file's own header flags a **stray draft** it found on disk, `VRS-Telecoms-prompt-85-uk-deaf-travellers-abroad.md`, as a number collision with Neurodivergence 85–91. I checked the prompts folder directly — **no such file currently exists**. Either it was never actually written or it has since been removed. Nothing to fix, but don't recreate a prompt under 85; that number belongs to Neurodivergence.

### Verdict for any public page

**Agree with the finding: curate first, draft almost nothing.** The safe lead sentence:

> The UK's inbound Deaf-access provision — 999 BSL, airport QR codes, NHS 111, the Accessible Information Standard — is built for British Sign Language. A visitor who signs ASL, International Sign, or another national sign language has no published UK public video-relay product to use.

### What already exists and should be linked, not rewritten

| Need | Point at |
|---|---|
| Emergency calling for a BSL-signing visitor | 999 BSL — no registration, no UK phone contract needed |
| Airport-floor help (BSL only) | Heathrow Convo Access QR; Manchester SignLive/QR |
| Urgent NHS advice (BSL only) | NHS 111 via SignVideo (registration required) |
| Text-based any-number calling regardless of sign language | Relay UK — but note the visitor-onboarding friction (needs a UK-reachable number to verify) |

### Don't list (confirmed sound)

Everything on the prompt's own don't-list is correctly drawn and worth keeping as written: don't claim the UK is accessible for Deaf tourists; don't claim 999 BSL works in ASL; don't treat AIS requirement 1.32 as a visitor-eligibility clause rather than an interpreter-qualification bar; don't import ADA/ACAA as UK law; don't invent a national ASL or International Sign interpreter roster; don't treat Ryanair's ISL listing as a general International Sign product.

### What to do with this finding

| Scenario | Action |
|---|---|
| Someone asks "can a Deaf tourist call 999 in the UK?" | Yes, via 999 BSL, but only for BSL — no registration or UK plan needed. |
| Someone asks whether an ASL or International Sign user has equivalent provision | No published product exists. Say so plainly; do not soften it into "limited support." |
| Someone wants to know if AIS protects a visiting patient | AIS attaches to being an NHS/social-care service user, not residency — but only for BSL/deafblind interpretation; other sign languages are out of scope by the standard's own drafting. |
| Someone wants a DeafBlind-visitor pathway | None exists beyond the general RIDB bench (19 nationally, three English regions at zero) and Contact Scotland's Braille-display path for BSL-using deafblind callers in that scheme. |

### What actually closes the gap (ranked)

1. **No new prompt needed on this question** — 84 closes the inbound-visitor scope this domain set out to answer.
2. **Fold into the existing FOI/right-of-reply plan** (already scoped in Grok's 78–80 feedback file) rather than opening a new visitor-specific tracker.
3. **A dated scrape of force-by-force 101 BSL listings and a foreign-SIM zero-rating test** are the two most answerable open items, per the prompt's own "what this prompt does not close" list — neither needs a new Grok prompt, both are volunteer/FOI-shaped tasks.

---

## Cross-batch rules

- Distinct from Access to Work (52–54) — that batch owns the cap/freeze/processing-time figures; this batch only adds the calling consequence.
- Distinct from HMRC (55–61) — HMRC's own SignVideo hosts are a Channel-C example, not a new finding.
- Distinct from Interpreter Regulation (81–83) — that batch's held-back lived-experience leg and this batch's held-back lived-experience leg are two separate unresolved items; do not conflate them or assume either has been issued a number.
- Distinct from AIS (34–37) and DeafBlind Adjustments (115–120) — prompt 84 reuses their findings (AIS scope text, RIDB headcount) rather than re-deriving them; don't recount RIDB from this file, recount from the Interpreter Regulation / DeafBlind Adjustments source instead.
- **This domain (78–80, 84) is now fully run.** The only open item is the never-numbered lived-experience leg — issue it from 164+ if it's picked up again; do not reuse 81 or 84.
