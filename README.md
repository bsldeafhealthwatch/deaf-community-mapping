# Deaf Community Mapping — BSL & Deaf Health Access

Working repository for the BSL & Deaf Health Watch evidence dossier and the research behind it. Empowering Deaf people to know and exercise their health access rights (Accessible Information Standard, BSL interpretation, and related entitlements) with sourced, dated, auditable evidence.

**Status: team-internal. Do not make this repo public yet.**

## Start here

- **`dossier/bsl_dossier.html`** — the public-facing evidence dossier. Open it directly in any browser (double-click, or drag into a browser tab). Contains: Know Your Rights, Evidence by Domain (16 researched domains), Contested & Unstable Figures, FOI Targets, and audience-specific pages for charities/businesses/policymakers/media. Has a search box for finding anything in the page.
  - **How editing works:** this file has no server backend. Using the in-page "Add"/"Edit" buttons saves changes to *your own browser's local storage only* — they are not shared with teammates automatically. To publish a change for the whole team, either edit the source data arrays directly in the HTML file (`DEFAULT_DOMAINS`, `DEFAULT_RIGHTS`, `DEFAULT_AUDIENCE` near the bottom of the file) and commit that, or use the in-page editor then export/copy your changes back into the file. If the team wants true shared live-editing later, that needs a small backend wired in (see the comment above `window.storage` in the file).

- **`research-framework/`** — the primary research. `BSL_DEAF_RESEARCH_FRAMEWORK.md` is the framework and next-steps doc; `VERIFICATION_STATUS.md` is the full verification log (every figure, checked against primary sources, dated); `BSL_DOMAIN_*.md` files are per-domain deep dives that feed the dossier's figures.

- **`foi-tracking/`** — FOI request planning and logs. `BSL-FOI-companion-log.xlsx` and `VRS-FOI-companion-log.xlsx` are the working trackers (send-ready, awaiting team review before anything is actually submitted — see each workbook's own instructions tab). `BSL-request-data-gap-tracker.docx` tracks what evidence gaps FOI requests are meant to close.

- **`healthcare-matrix/`, `healthcare-trackers/`, `stakeholder-maps/`** — supporting HTML trackers and maps built earlier in the project (multiple versions kept as the work progressed; the highest version number / most recent file is current).

- **`prompts/`** — prompt templates used for AI-assisted research (Grok/SuperGrok), kept for reproducibility so any finding can be traced back to how it was originally surfaced before verification.

- **`Claude outputs/`** — misc outputs from Claude-assisted research sessions.

## Working conventions already in use

- Files are backed up as `<filename>.bak-<timestamp>` before major edits. These backups are **not** tracked in git (see `.gitignore`) — they're a local safety net, not version history. Git itself is now your version history going forward.
- Every figure in the dossier and research framework carries a source, a URL where available, and a last-verified date. Figures unverified for 90+ days are flagged stale in the dossier automatically.
- Contested or unstable figures are logged openly (`research-framework/` domain files and the dossier's "Contested & unstable figures" section) rather than silently corrected — the correction process itself is meant to be auditable.

## Sharing

This repo is prepped for git but not yet pushed anywhere. When ready to share with the team: create a **private** GitHub repository, add teammates as collaborators, then push this folder. Do not make it public until the team has reviewed the FOI workbooks and agreed on what's ready for wider release — see `research-framework/BSL_DEAF_RESEARCH_FRAMEWORK.md` for current open items.
