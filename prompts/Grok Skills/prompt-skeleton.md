# Prompt skeleton (paste-into-Grok)

Copy this shape. One prompt = one dense paragraph, not bullets.

## Batch header (once per batch)

```
# Prompts NN–NN — <Topic>

Added: <date>. Covers <specific gap>.

Checked first: <index file + named cousin batches>. This is not a duplicate because <one sentence>. Distinct from prompts <NN–NN> because <life stage / jurisdiction / legal question>.

Anchor: <one concrete person/situation every prompt in this batch must stay honest to>.
```

If a Domain number is tempting, say whether this is a new domain, a stub under an existing cluster, or a cross-cut. Default is not a new domain.

## Each prompt

```
**NN. <short title>**
> As a UK <domain> researcher, using <named bodies — NHS England, CQC, PHSO, legislation.gov.uk, DWP, Ofcom, BDA, SignHealth, RNID, Sense, NRCPD, Hansard, academic literature>, establish (1) <definition or legal status>, (2) <the quantified or documentary evidence, including the date and whether the figure is official or advocacy>, (3) <the live fulfilment fact — who pays, who books, what happens when it fails>, and (4) <what is unpublished or contested>. Flag thin, unpublished, contested, or anecdotal evidence rather than presenting it as settled. For each element give source title, publishing body, publication or last-updated date, and a direct URL. Do not fill a UK cell with a US or other international figure; if only international material exists, label it international and record the UK cell as no reliable figure found.

Format your answer as a table with these exact columns: **Label | Value | Source name | Source URL | Publication date | Confidence (Verified/Contested/No reliable figure found)**.
```

Tighten the numbered sub-questions to the topic. Keep the persona, the flag-thin instruction, and the six-column line every time.

## Notes for this batch (required)

- Gate prompt — usually the definitions / legal-status one. Later prompts may not collapse the groups that prompt distinguished.
- Still-alive scepticism — any organisation catalogue. Volunteer groups go dormant without formally closing.
- Hard-don't — topic-specific public claim that must not be printed without a named statute, regulation, or judgment.
- Held-back legs — if lived experience or a public-draft prompt is deferred, say so and why.

## Findings-file addendum (Grok write-up, not the paste-in prompt)

When Grok (or a researcher) writes the *answer* to a numbered prompt in the artifacts workspace, do not use the dense paragraph. Use this shape, matching prompts 55 and 78

1. Title — `# Prompt NN — <question in plain language>`
2. Master-index line, batch range, compile date, dossier rule, lowest-tier rule.
3. **What this prompt is for** — one job. What must not be assumed.
4. **Index check** — the pack already lists these numbers / this file is the answer, not a new batch. Name any held-back prompt.
5. **Headline** — the verdict in short sentences. Gaps stay gaps.
6. **Findings table** — Label | Value | Source name | Source URL | Publication date | Confidence.
7. Numbered subsections (`NN.1`, `NN.2`) only where the argument needs room.
8. Do not invent a UK precedent. Do not overwrite a figure that already lives in an earlier project note without saying so.

Review mode then wraps a set of those files in the feedback skeleton. Do not flatten the per-prompt tables away when the topic is legal or procedural.
