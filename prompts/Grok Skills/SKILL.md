---
name: grok-research-prompt-batch
description: Use when writing a numbered SuperGrok research prompt batch for the Deaf Network Health Group BSL access dossier, or when reviewing Grok findings, Claude feedback, or a Don't list. Triggers include next batch, new domain gap, prompts for X, review this, findings review, and Claude feedback.
metadata:
  type: workflow
  version: "1.1"
  owners: Deaf Network Health Group
---

# Grok research prompt batch (Deaf Network Health Group)

Two modes. If the mode is not obvious, ask — Write a new prompt batch, or review findings Grok returned?

- Write mode triggers — next batch, new domain gap, prompts for X, a prompt number range.
- Review mode triggers — pasted Grok output, review this, Claude feedback, Don't list, findings.

## Locate the index first (both modes)

Do not invent a folder. Confirm against the files actually present this session.

- **Grok / this artifacts workspace** — master index is `artifacts/SuperGrok_Research_Prompt_Pack.md` (look for the NEXT PROMPT NUMBER line). Findings live as `artifacts/<Topic>-prompt-NN-slug.md`. Reviews live as `artifacts/<Topic>-prompts-NN-NN-claude-feedback.md`.
- **Claude project** — list project docs first. Historical names are `grok-prompts-<topic>.md` (prompts sent) and `grok-findings-<topic>.md` (reviews). A `claude/` prefix is valid only if those docs already exist.
- **DeafCommunityMapping local repo** (device bridge) — `prompts/SuperGrok_Research_Prompt_Pack.md` with the NEXT PROMPT NUMBER line. Read that file. Do not assume the number.

Read the index and the latest review file before writing anything. Never reconstruct a prompt number from chat memory.

## Write mode

1. Confirm a genuine gap. Check existing prompt / findings / feedback docs and the index for this topic or a close cousin. State in the batch opening what was checked and why it does not overlap. A variant (life stage, jurisdiction, legal question) must say how it differs. A cross-cut (CODA across AIS + safeguarding + SEND) is usually an addendum, not a new numbered Domain.
2. Number sequentially from the index, never from memory. Put the range in the batch header. The index NEXT PROMPT NUMBER line must be updated in the same edit that issues numbers.
3. Open with a framing paragraph — why the batch exists, what was checked, and a concrete anchor scenario if it keeps later prompts honest.
4. Decide the batch shape. Real batches have run 3–8 prompts. Logic, not a fixed count
   - Default four legs — definitions/scope → data/quantified evidence → comparative/international practice → lived experience/case for change.
   - Split a leg when one prompt would collapse distinct sub-groups, jurisdictions, or directions (hearing CODA vs Deaf-of-Deaf; England vs Scotland; UK resident abroad vs inbound visitor).
   - Hold the lived-experience prompt until the legal/data layer is closed. Say so in the batch if a leg is deferred.
   - Add a hard-constraints prompt (what must NOT be claimed publicly) when findings could feed a public page or template.
5. Write each prompt as one dense paragraph. Copy `references/prompt-skeleton.md`. Researcher persona naming real UK bodies → numbered sub-questions (1), (2), (3) → flag thin / unpublished / contested evidence, with source title, publishing body, date, and direct URL for each element.
6. Add Notes for this batch — load-bearing gate prompt (usually definitions), which catalogue needs still-active scepticism, and any topic-specific hard-don't.
7. End every prompt with the standard output line from the skeleton.
8. Save with the convention already in use in this workspace (see Locate the index). On Claude use the project's write tool. On Grok write under `/home/workdir/artifacts`. Do not create a parallel `claude/` tree on Grok.

## Review mode

When Grok output for a batch is pasted back

1. Never promote a Grok cell to settled fact. An unsourced AI claim is a gap to log, not a finding to restate.
2. Write the review using `references/feedback-skeleton.md` — headline verdict first (usually curate first, draft almost nothing), then scenario→action table, then the Don't list (do this before anything else), then what actually closes the gap ranked by concreteness (FOI in the existing tracker > link an existing resource > a new draft), then cross-batch rules.
3. For substantial legal or procedural findings, keep per-prompt source-register tables with the same six columns. That is why the AIS and Templates reviews stay usable.
4. Flag UK-thin cells filled by international (usually US) material. Label them international. They do not fill a UK data cell.
5. Save with the workspace convention. On Grok the review filename is `artifacts/<Topic>-prompts-NN-NN-claude-feedback.md`.

On Grok, findings Grok itself produces use a different shape from the paste-in prompt — headline, six-column table, numbered subsections. See `references/prompt-skeleton.md` (findings-file addendum). Do not flatten that shape when reviewing it.

## House rules (both modes)

- Never reconstruct a lost prompt number from chat memory. Re-read the index.
- Do not print illegal, non-compliant with the Act, duty of care breach, unregistered = criminal, or any similar legal conclusion without a named statute, regulation, or judgment. If the batch could support that kind of claim, that is what the hard-constraints prompt is for.
- England, Scotland, Wales and Northern Ireland are separate legal systems. A rule confirmed in one does not stand in for another. Scotland's NHS interpreting policy is the recurring example — do not paste it into an England-facing claim.
- International evidence is always labelled international. Context only, never a UK data cell.
- Before anything public, re-check live pages that move (interpreter registers, camp or event dates, framework supplier lists, benefit rates). A snapshot is dated, not current.
- FOI that falls out of a review goes into the existing FOI companion log / gap tracker, not a new one-off tracker and not a second FOI platform.
- Default public-facing verdict is curate first, draft almost nothing. Link a strong existing resource rather than drafting a rival, unless the findings show a genuine specific hole.
- Update the index NEXT PROMPT NUMBER line in the same edit that issues numbers.
- Dossier rule — stay unbiased, follow money and fulfilment, no DEI or anti-DEI banner.
