# Prompt 169 — Confidentiality when work text goes into a public cloud AI tool vs a local model

**Master index prompt 169.** Addendum to 134–140; pair with 168. Compiled 14 September 2026.

**What this prompt is for.** The same employee as 168 pastes the *employer’s* policy, email chain or report into a consumer chatbot to plain-English it. What do published UK employer / sector / ICO texts require? Is a local or tenant model treated as the documented mitigation? Do not repeat 137’s meeting-recording / Art. 21 analysis.

**Hard-don’t.** Do not print that using a public cloud tool on work documents is a data-protection breach, or that a local model resolves confidentiality, without a named policy or guidance document saying so.

---

## Headline

Published UK texts treat pasting employer or client material into an **unapproved consumer** chatbot the same way they treat pasting it into an unauthorised web translator: **outside the approved processor map**. That is policy and GDPR-governance language. It is not, in the sources opened, a judgment that the paste is automatically a personal-data breach.

Documented shape:

- **Approve a tool, or do not put confidential / personal data in it.** CIPD January 2025 workplace-AI guide is built around a permitted-tools policy for ChatGPT, Claude, Copilot and peers. CIPD Autumn 2025 LMO: staff already use free tools in 54% of organisations.
- **NHS example (named).** Rotherham Doncaster and South Humber NHS FT AI policy: ChatGPT and other public genAI **must not** process patient-identifiable, confidential or business-sensitive data. NHS England Digital Copilot IG: M365 Copilot sits in the tenant, is not a clinical system, does not train on org data; still not for clinical decisions. Same trust page: personal/sensitive patient information **may** go into Copilot but **must not** go into publicly available genAI.
- **ICO as employer.** ICO’s own internal AI-use policy (PDF, 2025/26): use AI on personal, sensitive or confidential information only when the ICO has permitted it through internal governance. Human review of outputs. That is the regulator’s staff rule, not a statutory “paste = breach” clause.
- **Same family as Grammarly / Google Translate.** Lawyer and template policies group unapproved cloud writing tools with unapproved third-party sites. No source found that carves out “but it is my reasonable adjustment” from the confidentiality rule.
- **Local / on-device model as mitigation.** Discussed as enterprise architecture (Samsung-style in-house after a leak; “on-prem” procurement). **No published UK text was found that treats a staff member’s self-hosted laptop LLM as the documented RA-plus-confidentiality fix, and no AtW award for one was found.** Tenant Copilot is the public-sector documented middle path — approved processor, not a local model.

Do not print lawful/unlawful. An employer policy can prohibit the paste. UK GDPR still needs a processor contract and a lawful basis if personal data leaves. Those are two different sentences.

---

## Findings table

| Label | Value | Source name | Source URL | Publication date | Confidence |
|---|---|---|---|---|---|
| CIPD workplace genAI policy ask | Guide on shaping an AI-use policy for consumer tools (ChatGPT, Claude, Copilot). Permitted tools / permitted uses. | CIPD *AI use in the workplace* | https://www.cipd.org/uk/knowledge/guides/preparing-organisation-AI-use/ | 23 Jan 2025 | **Verified** as CIPD guidance (member-gated body) |
| How many workplaces already see free-tool use | CIPD LMO Autumn 2025: employees using AI in 76% of organisations; 54% free tools; 42% paid including employee-paid. Public sector 87% vs private 73%. | CIPD LMO via Neathouse commentary | https://neathousepartners.com/blog/artificial-intelligence-when-is-an-employer-vicariously-liable | Autumn 2025 / commentary Jan 2026 | **Verified** as CIPD survey figures via secondary. Re-open CIPD primary before public reuse |
| ICO staff rule (not a general DN) | Use AI involving personal, sensitive or confidential information only when permitted through ICO internal governance. Human review. | ICO *Internal AI use policy* PDF | https://ico.org.uk/media2/u3ad0ucv/internal-ai-use-policy.pdf | Policy Aug 2025 / PDF seen Apr 2026 | **Verified** as ICO-as-employer. Not a public Decision Notice on a staff ChatGPT paste |
| ICO public AI-and-DP guidance | Best-practice interpretation of UK GDPR for AI systems. Not a statutory code. Does not name “employee pastes the board pack into free ChatGPT” as a worked RA exception. | ICO *Guidance on AI and data protection* | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/ | Live 2026 | **Verified** as general. Worked employee-paste example unpublished |
| Named NHS trust public-genAI ban on confidential text | RDaSH: ChatGPT and other public genAI must not process PID, confidential or business-sensitive data, or write clinical records. Copilot treated differently (tenant). | RDaSH *Artificial intelligence (AI) policy* | https://www.rdash.nhs.uk/policies/artificial-intelligence-ai-policy/ | Page live Sep 2026 | **Verified** as one NHS FT policy |
| NHS England Copilot IG | M365 Copilot: not a clinical system; does not train on org data; staff must check outputs; not for clinical decisions. | NHS England Digital *Microsoft 365 Copilot information governance guidance* | https://digital.nhs.uk/data-and-information/information-governance/guidance/microsoft-365-copilot | Live 2026 | **Verified** as national IG for the *tenant* product |
| Same as unauthorised translator / grammar site? | Template and firm commentary group unapproved consumer AI with unapproved third-party web tools: no processor contract, possible training on inputs, confidentiality leaves the organisation. No source carves out a BSL-adjustment exception. | CIPD-shaped templates; EM Law; Mondaq grievance/AI note | e.g. https://emlaw.co.uk/ai-in-the-workplace-how-to-use-it-responsibly/ | 2025–26 | **Verified** as common policy pattern. Not an ICO ruling |
| Local / self-hosted model as documented RA mitigation | **Not found** as a published UK RA-plus-confidentiality product. Tenant Copilot / enterprise ChatGPT Team with a DPA is the documented middle path. In-house models appear as enterprise procurement after leaks (Samsung 2023 is international). | This-pass search; ICO internal policy; NHS Copilot IG | — | 14 Sep 2026 | **No reliable figure found** for AtW- or employer-funded staff laptop LLM |
| AtW funded a local model for confidentiality | **Not found.** | Prompt 168 SAE search | — | 14 Sep 2026 | **No reliable figure found** |
| ACAS | Advises employers to have clear AI-use policies (via secondary). Draft disciplinary/grievance Code consult (to 23 Sep 2026) *asks* whether the Code should address AI — it does not yet set the paste rule. | ACAS consult; Walker Morris | https://www.acas.org.uk/about-us/acas-consultations/code-of-practice-disciplinary-grievance-2026 | Consult 30 Jul–23 Sep 2026 | **Verified** as consult question, not a finished rule |
| Consumer-tool terms (comparison, not endorsement) | Free consumer accounts may use inputs to train unless the user opts out; business/enterprise tiers typically contract no-training + a DPA. Exact terms move — re-open the vendor page before citing a clause. | OpenAI / vendor terms generally; CIPD-shaped commentary | — | 2026 | **Contested** if a specific clause is printed without the live URL |
| NZ ERA 2025 GenAI + confidential dispute docs | International. Authority drew a line at uploading employer confidential material to OpenAI; did not ban AI outright. | LinkedIn / NZERA 716 commentary | International | 2025 | International only |
| Prompt 137 | Meeting recording, Art. 21, Teams consent-gate. Different object. | Prompt 137 | — | 11 Sep 2026 | Do not repeat |

---

## 169.1 Two sentences that must stay separate

1. **Policy.** A named employer or sector body can prohibit unapproved cloud tools for confidential text. RDaSH does. CIPD tells HR to write that list.
2. **UK GDPR.** If the paste includes personal data, the employer is still the controller and needs a processor relationship it can stand behind. ICO has not published a Decision Notice that the paste is always a breach.

A local model that never leaves the device changes the *processor* map. No source found that AtW will buy one so a BSL-first employee can plain-English the staff handbook.

---

## 169.2 Collision with 168

168’s unpublished cell is “is this an adjustment.” 169’s published cell is “unapproved cloud tools are treated like any other unapproved website.” An adjustment argument does not, in any opened UK text, punch a hole in that policy. The practical grey zone is already named in MoleWorks 2025: AtW/DSA recommend a cloud writing tool; IT refuses it.

Do not draft a public card that says “use Claude on the policy PDF, it is your right.” Do not draft one that says “using Claude is a breach.” Point at the employer’s approved-tool list and, if there is none, at CIPD + the named NHS distinction between tenant Copilot and public ChatGPT.
