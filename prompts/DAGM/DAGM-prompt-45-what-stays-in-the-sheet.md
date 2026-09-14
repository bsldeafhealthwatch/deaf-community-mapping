# Prompt 45 — What stays in the sheet until a host appears

**Master index prompt 45.** Eighth and last file in the Deaf Access Gap Monitor / BSL Policy Maker scoping batch (prompts 38–45). Compiled 8–9 September 2026. Dossier rule: stay unbiased; follow money and fulfilment. An unsourced AI claim is the lowest tier. Gaps are logged as gaps.

**What this prompt is for.** Prompt 44 priced the cash that buys a first public table. This file names the technical objects that money is *not* buying — a query API, a parser, a hosted marking tool, a multi-user CMS — and says what the durable layer is until a funded host appears. It does not specify a stack. It says which layer the cousins actually lived on at the equivalent stage, and which layer this dossier is already on.

---

## Headline

CAPE’s own data page still says the quiet part: “Much of our data is crowdsourced by an army of volunteers filling in **Google spreadsheets**. This is then combined with some standard data to enable it to be matched up across sources.” The explorer and the “rudimentary API” came after mySociety turned those sheets into a database. The sheets were the product for a year.

Institute for Government Performance Tracker 2025 uses “more than 250 indicators.” The main output is still **an annual PDF report**. Full Fact’s corrections layer is a dated HTML log and a feedback form, not a query endpoint. Public Whip had a parser only because Hansard was one repeating official feed.

This project’s sources are FOI PDFs, award notices, AIS self-assessments, Charity Commission accounts and register scrapes. They are not one feed. A parser that “ingests UK policy, legal and budget data” is a sentence from the working pitch, not a week-one object. The objects that already exist — `BSL-FOI-companion-log.xlsx`, the gap tracker, the agency workbook, the filterable matrix HTML, the prompt-34-to-44 markdown — *are* the sheet. The next technical job is to freeze columns and identifiers so a second year can be compared, then put a static page over one scored table. The API waits for a host.

---

## 45.1 What each cousin actually stored at v1

| Cousin | Storage at first public version | When a queryable layer appeared | Trigger |
|---|---|---|---|
| Public Whip (2003) | Parser → MySQL → PHP pages | The site *was* the query. No long private sheet. | Possible only because Hansard is one feed. |
| TheyWorkForYou (Jun 2004) | Front-end on that parser | DCA-funded API, summer 2006 — two years later, after mySociety adoption | Grant + host, not a rewrite. |
| Climate Emergency UK (2019) | Website + spreadsheets of declarations | CAPE explorer 2020 (mySociety `caps` repo). Scorecards site later. Data page still describes Google Sheets as the capture layer. 2022 scorecard data published as CSV tables (authority scores, individual answers, questions list). API described by mySociety as “rudimentary.” | Partnership. Sheets survived the partnership. |
| WhatDoTheyKnow (Feb 2008) | Rails app, one request = one record | The archive *is* the database, grown from use | Pattern 2 (user creates the row). Not copyable here. |
| FixMyStreet (2007) | One report = one row | Council white-label / SocietyWorks later | Same pattern 2. |
| Full Fact | CMS articles + a public corrections log (dated HTML list, last-3-years page live Sep 2026) | ClaimReview markup as plumbing for platforms, not a public query API for researchers | Newsroom, not a scorecard. |
| IfG Performance Tracker | Analyst workbook behind an annual report | No public query API found on this pass. 2025 edition is a PDF. Shorter follow-up papers reuse the same internal store. | Already-funded think tank. The “tracker” is a publication series. |
| PledgeBank | A general pledge platform | Closed 2015 so the parent could concentrate | The failure mode: platform before a narrow job. |

The pattern that maps onto this dossier is CE UK 2019–20, not Public Whip 2003 and not TheyWorkForYou’s 2006 API.

---

## 45.2 Why a parser is the wrong first object

Public Whip worked because the input was one publisher, one format family, one repeating event (a division). TheyWorkForYou inherited that.

This project’s inputs, already logged across the dossier:

- ICB / trust FOI replies as PDF or email, sometimes a password portal (prompt 43: reject the portal).
- Find-a-Tender / Contracts Finder award notices with BSL not itemised.
- AIS self-assessments, when published, in whatever CMS the body uses.
- NRCPD register counts (manual pull, dated).
- Charity Commission and Companies House accounts.
- ONS / LG Inform population denominators.
- Lived-experience findings that are PHSO / CQC / named first-person pieces, not a feed.

There is no single “ingest UK policy, legal and budget data” pipe. A scraper that pretends there is one will invent rows. The dossier rule forbids that.

CAPE’s middle layer is the honest comparison: volunteers find the PDF, paste the URL into a sheet, staff add the GSS code, mySociety later loads the file into a search index. The “database” is a well-labelled pile of documents plus a join key. That is achievable here with ODS codes (trusts), ICB organisation codes, local-authority GSS / three-letter codes, and a WhatDoTheyKnow URL per request. It does not require `script/update --all`.

---

## 45.3 The sheet that already exists

Do not start a second store. Freeze these and keep them in one place.

| File already in `/home/workdir/artifacts` | What it is in CAPE vocabulary | What to freeze |
|---|---|---|
| `BSL-FOI-companion-log.xlsx` | The request ledger | One row per authority-wave. Columns: body legal name, ODS/ICB/GSS code, template used, WDTK URL, sent date, due date, status, refusal ground, figure, unit, period, reply-override flag, reply date, annotation URL. Collapse T1–T6 into one letter per body (prompt 43) but keep tabs internally if useful. |
| `BSL-request-data-gap-tracker.docx` | The known-unknowns list | “Not found at URL on DATE” as the unit. Do not promote a gap to a number. |
| `SWL-SEL-BSL-interpreting-agencies.xlsx` | The contractor register | Company number, award notice URL, dates, whether BSL is itemised. DAL / Sign Solutions / LanguageLine / thebigword cells already live here. |
| `deaf-healthcare-swl-matrix-v9.html` | The stakeholder map, not the score | Keep power×interest tags. Do not turn this into a compliance RAG. |
| AIS / DAGM markdown briefs (34–44) | Methodology and legal constraints | These *are* the published method once a table goes public. Do not rewrite them into app copy. |
| `SWL-BSL-what-fails-what-succeeds.docx` | Cost diagnosis | MODELLED cells stay labelled MODELLED. |

Minimum columns on any scored table that leaves the sheet:

1. Body legal name  
2. Persistent code (ODS for a trust, ICB code, GSS for a council)  
3. Question id (frozen; versioned)  
4. Cell value, or one of: found / not found / refused / not applicable  
5. Source URL  
6. Source date  
7. First-mark date  
8. Right-of-reply offered (Y/N, date)  
9. Reply received (Y/N, date)  
10. Value after reply (may differ; do not delete the first)  
11. Marker initials, auditor initials  
12. Notes that are not the score  

That is the 2022 Scorecards “individual answers” CSV, shrunk to this domain. CE UK published exactly those three tables: questions list, individual answers, authority scores. Copy the shape. Do not copy 93 questions.

---

## 45.4 What a first public page can be without an API

A static page is enough and is what several cousins shipped.

Acceptable v1, in order of labour:

1. **A dated HTML table** with the twelve columns above, for the SWL cluster plus named comparators, plus a methodology page that is this batch’s rules in public language. The matrix HTML already proves the environment can ship a page.
2. **A CSV zip** in the CAPE style: `questions.csv`, `answers.csv`, `bodies.csv`. Licence it. That is what journalists actually reused from Scorecards (prompt 41, *FT* from the FOI trail).
3. **WDTK links as the raw evidence**, not a home-built archive. The pipe exists.

Not v1:

- Postcode lookup. CAPE has this because every resident has a council. AIS fulfilment is not a postcode fact.
- User accounts, marking UI, role-based access.
- A JSON API “for charities and Parliament to query.” mySociety called CAPE’s own API rudimentary *after* the explorer existed. IfG still has not shipped one for 250 indicators.
- Search across every AIS PDF in England. That is CAPE-after-host work (`script/update`, Solr/Elastic, MapIt keys).
- Auto-scoring from text. Still Ignored and Locked Out are snapshots; they are not a model.

A Google Sheet published to the web, with the twelve columns locked and a tab for the method, is a valid v1. Embarrassing is not the test. Comparable is the test.

---

## 45.5 Join keys, not a knowledge graph

CAPE works because every row carries a GSS code and a three-letter council code. This project needs the equivalent, written down once:

- NHS trusts and foundation trusts: ODS code.  
- ICBs: the statutory name after the 1 April 2026 Order, plus the ODS/ICB code. Clustered SWL/SEL is one statutory body with two historic geographies — do not double-count.  
- Councils / CASSRs: GSS and the WDTK three-letter code where it exists.  
- Companies: Companies House number (DAL 06207784 already in project memory).  
- Evidence: the WhatDoTheyKnow request URL, not a pasted paragraph.

Do not invent a “Deaf access ontology.” Do not build a graph database. The join is a code in a column.

---

## 45.6 What not to build, and why

| Object | Why it waits | What breaks if it is built now |
|---|---|---|
| Public query API | No host, no stable schema, no second-year comparison | You maintain an interface onto cells that the right-of-reply will change. CE UK lets the reply override the FOI; an API that cached the first mark would publish the wrong number. |
| Custom parser / “ingest engine” | Inputs are not one feed | Invented rows. Violates the source hierarchy. |
| Hosted marking tool | Cycle 0 is one person and a 16-row log | You spend the £10–20k seed on software instead of BSL for a lived-experience session and the five-week reply letters (prompt 44). |
| Second FOI platform | WDTK exists; Pro is £200/year | PledgeBank. |
| RAG “compliance” dashboard | Prompt 39 killed official-sounding names; prompt 42 forbids “non-compliant with the Act” as a volunteer conclusion | Readers think CQC has spoken. That is a legal-adjacent problem, not a UI problem. |
| User-generated gap reports | Pattern 2. Works for lamps and FOI requests. Does not work for AIS-versus-spend facts. | Unsourced lived-experience rows sitting next to the 878 gold cell. |
| AI-filled cells | Explicitly the lowest tier in this dossier | A number with no URL. |

The working name “BSL Policy Maker” is a later-phase query fantasy. Prompt 38–39 already treated it as a name, not an architecture. Keep it that way.

---

## 45.7 The host is the jump, not the repo

CAPE’s GitHub (`mysociety/caps`) is a Django app with Vagrant/Docker, MapIt, and `script/update --all`. It exists because mySociety approached CE UK in 2020 and put engineers on a collection that already had sheets. TheyWorkForYou’s API exists because the DCA paid for it after adoption. IfG never needed an API because the host *is* the publication channel.

Until a host with engineers appears — mySociety-shaped, university-shaped, or a Deaf-sector body that already runs a site — the technical path is:

1. Freeze question ids and the twelve columns.  
2. Run the prompt-43 loop on the SWL cluster.  
3. Publish the table and the CSV.  
4. Keep the sheet as the system of record through the reply window.  
5. Do not migrate to a database because it feels more serious.

A repo of the markdown briefs plus the CSV is a reasonable public artefact. A repo of an empty Django app is not.

---

## 45.8 What prompts 38–45 together allow, and what they close

Allowed now, without new money beyond prompt 44’s cycle-0 cash:

- Keep collecting in the existing workbooks.  
- Freeze a short question set.  
- Send one combined FOI per named SWL / comparator body via WhatDoTheyKnow.  
- Offer a five-week right of reply.  
- Publish a static table + CSV + methodology, under a name that is not official-sounding (prompt 39).  
- Label every modelled cell. Log every gap as a gap.

Closed until a host and a second cycle exist:

- A public query product for “charities, local authorities, possibly Parliament.”  
- A national 36-ICB + 205-trust score presented as a platform.  
- A parser.  
- A compliance monitor badge.  
- A grant application written as if the platform were the deliverable.

The original pitch asked whether the idea was scalable without breaking the dossier. The answer from this batch: the *collection method* scales the way CE UK scaled — questions, WDTK, reply, audit — and only at that labour price. The *query platform* is a different object, owned in every durable case by a host that already had staff. Building the second object first is how PledgeBank spent a decade. The dossier’s source hierarchy survives if and only if the sheet remains the system of record.

---

## 45.9 Search log

Checked 8–9 September 2026: CAPE data page (Google Sheets as capture layer; CSV downloads with GSS codes); mySociety CAPE product page and “rudimentary API” line; `github.com/mysociety/caps` README (`script/update --all`, MapIt); 2022 Scorecard data site (authority scores / individual answers / questions list CSVs); IfG Performance Tracker 2025 page and PDF (250 indicators, annual report as main output; no public API found); Full Fact feedback and corrections-log pages; existing artefact list under `/home/workdir/artifacts`. Public Whip / TheyWorkForYou parser history as already sourced in prompt 40.

**Gaps.**

- Exact year CAPE’s Google Sheets stopped being the write-layer and became an export. The 2026 data page still describes sheets as the capture method.
- Whether councilclimatescorecards.uk is a separate app from `caps` or a skin on the same database: not pulled to a commit-level answer on this pass.
- IfG internal store format (Excel, Tableau, warehouse): not published.
- No NHS-ODS + ICB-code lookup already sitting in this repo. That join file is a cycle-1 task, not a found artefact.

---

*End of prompts 38–45.*
