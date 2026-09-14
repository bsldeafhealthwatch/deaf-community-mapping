# Private hosting options for the BSL & Deaf Health dossier

**For team discussion — September 2026**

## Where we are now

The dossier is live on GitHub Pages: `bsldeafhealthwatch.github.io/deaf-community-mapping/dossier/bsl_dossier.html`. It's technically **public** — GitHub's free plan only serves Pages sites from public repos — but kept low-profile with a `robots.txt` block and `noindex` tags so search engines won't index it. Anyone who gets the exact URL can open it; there's no login or password. Graeme is the only editor: updates mean editing the HTML directly and pushing to GitHub.

If the team wants the dossier genuinely private rather than "public but hidden," here are the three realistic options, sized for a team of **up to 6 people**.

## Option 1: Cloudflare Pages + password (smallest change)

Keeps the dossier exactly as it is — same hand-built HTML, same accessibility work (skip links, ARIA landmarks, search box, hash deep-links), same git workflow. The only change is where it's hosted and a login screen in front of it.

**How it works:** Push to GitHub (repo can now be made private) → Cloudflare Pages builds and deploys automatically, the same way GitHub Pages does now → Cloudflare Access sits in front of the published site and requires a login before anyone sees a page.

**Access control:** Cloudflare Access (their Zero Trust product) is free for up to 50 users — 6 people is well within that. Two ways to gate it:
- One-time PIN by email: each person enters their email, gets a code, no account or password to remember or manage.
- A single shared password, if you'd rather skip per-person setup entirely.

**Cost:** Free at this scale (Cloudflare Pages hosting is free; Access is free under 50 users).

**What changes for the team:** Nothing about editing. Graeme stays the sole technical operator — repo owner, configures Access — same as today.

**What it doesn't solve:** The single-editor bottleneck. If the team wants others to update content without going through Graeme and git, this option doesn't help with that.

## Option 2: GitBook (keeps a GitHub-based workflow, opens up editing)

GitBook syncs with a GitHub repo — push Markdown files, GitBook renders and publishes a site from them, and edits made in GitBook's own editor can sync back to GitHub as commits. Closest of the "real migration" options to what you have now, workflow-wise.

**The catch:** GitBook renders from Markdown, not arbitrary HTML/JS. The dossier's custom interactive bits — the search box, ARIA tabs, hash-based routing — don't transfer directly and would need to be rebuilt as GitBook content, relying on GitBook's own (decent, but not custom-built) theme and accessibility handling. The FOI tracker spreadsheets would need to become GitBook tables or stay as separately linked downloads.

**Access control:** Private spaces shared by invite (email or link) on GitBook's free/personal tier — genuinely private, no public exposure at all.

**Cost:** Free tier likely covers a 6-person private space; GitBook's paid tiers exist if the team outgrows it, but shouldn't be needed at this size.

**What changes for the team:** Non-technical members could edit directly in GitBook's editor without touching git or HTML — solves the sole-editor bottleneck. Trade-off is the rebuild effort and losing the bespoke HTML/accessibility work as originally built.

## Option 3: Notion (easiest editing, biggest rebuild, no GitHub integration)

Notion is not a static-site host and does not integrate with GitHub for this purpose — there's a GitHub connector, but it pulls issues/PRs into Notion, it doesn't publish HTML pages from a repo. Moving the dossier here means manually recreating it as Notion pages: copy-pasting text, re-embedding images, rebuilding the FOI trackers as Notion databases. Not a sync, a rebuild.

**Access control:** Invite-only by default, free plan covers up to 10 guests — 6 fits comfortably. No public URL exists unless the team deliberately shares one.

**Cost:** Free at this scale.

**What changes for the team:** Any of the 6 could edit any page directly, no git or HTML needed at all — the most editor-friendly option. But the dossier's custom HTML/CSS/JS (the accessibility work, the search, the interactive tabs) doesn't come along — you'd be relying entirely on Notion's own page rendering and accessibility profile instead of the one built specifically for this project.

## Summary comparison

| | Cloudflare Pages + password | GitBook | Notion |
|---|---|---|---|
| Keeps current HTML/accessibility build | Yes, unchanged | No — rebuild in Markdown | No — rebuild in Notion blocks |
| Git-based workflow | Yes, same as now | Yes, syncs with GitHub | No |
| Non-technical team members can edit | No — still needs git/HTML | Yes, in GitBook's editor | Yes, most direct |
| Genuinely private (not just hidden) | Yes | Yes | Yes |
| Migration effort | Minimal | Moderate | Highest |
| Cost at 6 people | Free | Free | Free |

## Suggested framing for the team discussion

The real decision isn't really "which platform" — it's **whether privacy alone is the goal, or whether spreading out editing beyond Graeme matters too.**

- Privacy only, keep everything else as-is → **Cloudflare Pages + password**.
- Privacy *and* want others able to edit without git/HTML → **GitBook** (partial rebuild, keeps closer to current structure) or **Notion** (full rebuild, easiest ongoing editing).
