# Prompt 40 — Staged build path: what similar tools actually shipped first

**Master index prompt 40.** Third file in the Deaf Access Gap Monitor / BSL Policy Maker scoping batch (prompts 38–45). Compiled 8–9 September 2026. Dossier rule: stay unbiased; follow money and fulfilment. An unsourced AI claim is the lowest tier. Gaps are logged as gaps.

**What this prompt is for.** Separate the origin story that gets told later from the thing that actually existed in week one. The question for this project is not “what should the finished platform look like.” It is “what did the tools we would copy *do first*, how long did they stay manual, what triggered the jump to a public interface, and what happened to anyone who skipped the middle.”

**Closest cousins used here.** mySociety (TheyWorkForYou, WhatDoTheyKnow, FixMyStreet, PledgeBank), Public Whip, Climate Emergency UK / CAPE / Council Climate Scorecards, Full Fact, Institute for Government Performance Tracker and Whitehall Monitor. MIT Promise Tracker already covered in prompt 38 (lab project, 2013–2018, then archived).

---

## Headline

Every durable UK accountability tool in this set had a *working dataset or working transaction* before it had a polished public query product. None of them began as “a platform charities and Parliament can query.”

Two patterns repeat:

1. **Scrape / collect first, interface second.** Public Whip (summer 2003) was two people parsing Hansard into MySQL. TheyWorkForYou (June 2004) was a public front-end on top of that parser. Climate Emergency UK (2019) was a website plus spreadsheets of council declarations. CAPE and the Scorecards came later, after mySociety turned the collection into a database.
2. **Ship a thin public transaction, not a complete dataset.** FixMyStreet (Feb–March 2007) and WhatDoTheyKnow (Feb 2008) went public as soon as one user could complete one action (report a lamp; file an FOI). The archive *grew from use*. That only works when the user *creates* the record. It does not work when the record is a policy-versus-spend fact that has to be extracted from PDFs and FOI replies first.

This project is pattern 1. The SWL 878 series, the FOI companion log and the AIS / DWP / Jobcentre briefs already *are* the manual stage. The documented jump trigger in pattern-1 tools is almost never “we finished the architecture.” It is a grant, a partnership, or an external event that made the collection suddenly worth scoring.

Tools that skipped a narrow first job and tried to be a general civic platform (PledgeBank) ran for years and were then closed so the organisation could concentrate. That is the documented failure mode, not “they launched a website too soon.”

---

## 40.1 TheyWorkForYou — volunteer site on top of an already-running parser

**Actual v1.** Not a spreadsheet. A public website launched **6 June 2004** at the NotCon04 conference, built by “a dozen or so volunteers” who had already shipped FaxYourMP and Public Whip. The June 2004 “About” page lists them by name and says one developer was kept fed for a month by a small UK Citizens Online Democracy grant. Hansard was scraped under Crown copyright; they launched anyway.

**The stage before v1.** **Public Whip**, started summer 2003 by Francis Irving and Julian Todd after the 18 March 2003 Iraq-war division. Perl (then Python) downloaded Hansard, extracted votes, loaded MySQL, displayed through PHP. Never grant-funded; founders paid server costs. By late 2003 it also parsed written answers. The Parliamentary Parser that still feeds TheyWorkForYou grew out of that work. TheyWorkForYou is the readable front-end; Public Whip is the vote database. Treating TheyWorkForYou as if it appeared from nowhere in 2004 erases a year of two-person scraping.

**Manual period before a public query interface.** Public Whip was itself public within months of the idea. There was no long private-spreadsheet phase. The “personal” phase was two people writing a parser in spare time.

**What triggered the jump to a maintained public product.** mySociety adopted TheyWorkForYou in **early 2006** (about 20 months after launch). Summer 2006: Department for Constitutional Affairs funded an API. Channel 4 ran a branded election version in 2005. Adoption by a funded organisation, not a rewrite, is what turned a volunteer conference launch into a standing service.

**Idea → first public version.** Iraq vote 18 March 2003 → Public Whip summer 2003 (roughly 3–6 months). Parser work through 2003 → TheyWorkForYou 6 June 2004 (about 12 months of volunteer build).

**First public version → institutional recognition.** Channel 4 reuse by April–May 2005 (~10–11 months). DCA API summer 2006 (~24 months). Lord Gould of Brookwood, in a Lords debate on the Power Inquiry, called TheyWorkForYou and the other mySociety sites “probably the biggest single catalyst for political change in this country” (commonly dated to that mid-2000s Power Inquiry period; treat the wording as contemporaneous praise, not a measured impact study). Tobias Escher’s 2011 mySociety-commissioned research report is the first substantial independent evaluation.

**Sources**

- About us — TheyWorkForYou, captured 30 June 2004. “A dozen or so volunteers… One of our key developers was kept fed for a month by a small grant from UK Citizen’s Online Democracy.” <https://web.archive.org/web/20040630041815/http://www.theyworkforyou.com/about/>
- TheyWorkForYou research report — Tobias Escher, 2011. Launch 6 June 2004; mySociety adoption early 2006. <https://www.mysociety.org/files/2011/06/TheyWorkForYou_research_report-2011-Tobias-Escher1.pdf>
- Public Whip — Wikipedia / project FAQ. Started 2003 after the Iraq division; never grant-funded; handed to a new team 1 Aug 2011. <https://en.wikipedia.org/wiki/Public_Whip> <https://www.publicwhip.org.uk/faq.php>
- United Kingdom’s TheyWorkForYou — GovLab ODImpact case. Launch June 2004; Crown-copyright scrape; Steinberg later commissioned to co-write the Power of Information review because Number 10 staff used the site. <https://odimpact.org/case-united-kingdoms-theyworkforyou.html>
- mySociety history page. TheyWorkForYou launches June 2004 (not yet a mySociety project); adopted April 2006. <https://www.mysociety.org/about/history/>

---

## 40.2 WhatDoTheyKnow — 18-month build, thin public launch

**Actual v1.** A working FOI-filing website launched **22 February 2008**. Tom Steinberg’s launch line, preserved by mySociety: it “doesn’t have a name yet, nor any slick design, nor half the features we want it to have, but it works and it gets things done.” The public interface *was* v1. The archive did not exist until people used the filer.

**The stage before v1.** Not a private spreadsheet of FOI replies. A 2006 public call for the next mySociety project. Francis Irving and Phil Rodgers independently proposed an “FOI Filer and Archive.” Joseph Rowntree Reform Trust funding was in place by December 2006. That month mySociety was already asking supporters for example requests so the tool could be designed around real wording. FOI law itself had only been in force since 1 January 2005.

**Manual period before a public query interface.** None, in the Climate-Scorecards sense. About **18 months of funded development** between idea-selected and launch. Volunteer labour has been the *ongoing* operating model, not the pre-launch model.

**What triggered the jump.** A competition winner plus a named grant (JRRT), then 18 months of build. The “jump” is the launch itself. Public authorities were not universally delighted that requests and replies would sit in public; that friction is documented from the first year.

**Idea → first public version.** 2006 call / late-2006 funding → 22 February 2008 (~14–18 months).

**First public version → institutional recognition.** New Media Awards 2008 (Innovation winner; Democracy in Action finalist). Volunteer Alex Skene gave evidence to the Justice Committee’s post-legislative scrutiny of FOI on **21 February 2012** — four years after launch. Alaveteli, the reusable codebase, was cloned for Kosovo in 2009–10 and later powered 26 sites (figure as at January 2018). Running-cost figure published for 2011: around £12,000 a year.

**Sources**

- Timeline: FOI and WhatDoTheyKnow — mySociety, 22 February 2018. 2006 idea; JRRT funding; ~18 months’ development; launch 22 Feb 2008 with Steinberg’s “no slick design” line. <https://www.mysociety.org/timeline-foi-and-whatdotheyknow/>
- Ten years of WhatDoTheyKnow — mySociety, 22 February 2018. <https://www.mysociety.org/2018/02/22/ten-years-of-whatdotheyknow/>
- What we want to know about WhatDoTheyKnow — mySociety, 5 April 2023. Restates the 2006 “FOI Filer and Archive” brief. <https://www.mysociety.org/2023/04/05/what-we-want-to-know-about-whatdotheyknow/>
- WhatDoTheyKnow — Wikipedia. Launch 25 Feb 2008 on the wiki; 21 Feb 2012 Justice Committee evidence; 2011 running cost ~£12k. <https://en.wikipedia.org/wiki/WhatDoTheyKnow>

---

## 40.3 FixMyStreet — grant, beta report, public in weeks

**Actual v1.** A map-and-email site. First public report **2 February 2007** (broken light on a canal footbridge, Oxford — filed in beta by a staff member; council fixed it). Official launch **March 2007** as Neighbourhood Fix-It. Renamed FixMyStreet **June 2007** when the domain became free. Code by Francis Irving, Matthew Somerville and Chris Lightfoot, with the Young Foundation. Funded by the Department for Constitutional Affairs Innovations Fund — contemporaneous press says **£10,000**.

**The stage before v1.** Steinberg’s stated spark: smashed phone boxes on a three-week cycle; when he rang the council, complaints were confidential so he could not see whether anyone had already reported them. That is an anecdote, not a spreadsheet. There was no multi-year private dataset. The site *created* the public dataset by publishing the reports.

**Manual period before a public query interface.** Days to weeks of beta, not years.

**What triggered the jump.** A small government innovations grant plus a team that had already shipped TheyWorkForYou and WriteToThem. *The Times*, 21 April 2007 (“Web watchdog that shames councils into swifter action”): about 2,000 reports since February, ~10% marked fixed; some councils asked “who gave you permission.” One thousand reports in the first week after official launch (mySociety retrospective).

**Idea → first public version.** Grant + build → February/March 2007. Measured in months, not years. The prior “idea time” is not given as a dated private prototype.

**First public version → institutional recognition.** National press within 6–8 weeks. iPhone app December 2008. Councils later adopted the codebase as their own reporting front-end (Bristol, Oxfordshire and others in later retrospectives). One million UK reports celebrated July 2017.

**Sources**

- Happy birthday FixMyStreet — mySociety, 3 February 2017. First public report 2 Feb 2007. <https://www.mysociety.org/2017/02/03/happy-birthday-fixmystreet/>
- The big one million — mySociety, 21 July 2017. Beta lamp; March launch as Neighbourhood Fix-It; 1,000 reports in a week. <https://www.mysociety.org/2017/07/21/the-big-one-million-celebrating-fixmystreet/>
- FixMyStreet rename — mySociety, 16 June 2007. <https://www.mysociety.org/2007/06/16/fixmystreet/>
- Web watchdog that shames councils — *The Times*, 21 April 2007. £10,000 grant; Steinberg phone-box origin; council suspicion. <https://www.thetimes.com/uk/politics/article/web-watchdog-that-shames-councils-into-swifter-action-3wq5z80p98w>
- FixMyStreet.com — Wikipedia. DCA Innovations Fund; Irving / Somerville / Lightfoot; Young Foundation. <https://en.wikipedia.org/wiki/FixMyStreet.com>
- mySociety history. Neighbourhood Fix-It March 2007; rename June 2007. <https://www.mysociety.org/about/history/>

---

## 40.4 Climate Emergency UK / CAPE / Scorecards — the closest method cousin

This is the project that most resembles a BSL policy-vs-delivery monitor: a published standard-like question set, every council, volunteer marking, FOI at scale, right of reply, then a public score.

**Actual v1.** Not a query platform. A **2019 website** set up by then-Lancaster councillor (later CE UK founder) to record climate-emergency *declarations* so that declaring would look mainstream rather than factional. Resources and contacts for other councillors. Volunteers, overworked. The underlying store in the CAPE era is described by a mySociety engineer as “hand-updated Google Spreadsheets” of plans, declarations and net-zero pledges, plus official emissions tables.

**What triggered the jump.** mySociety approached CE UK in **2020** (first year of the site). Partnership produced **CAPE** (Climate Action Plan Explorer). re3data records CAPE as started **3 September 2020**. CAPE made the collection searchable. Then:

| Date | What shipped | What it was |
|---|---|---|
| Jan 2022 | Council Climate *Plan* Scorecards | Strength of written plans, not delivery |
| Oct 2023 | Council Climate *Action* Scorecards | First UK-wide score of completed action; FOI via WhatDoTheyKnow; volunteer first-mark; council right of reply |
| Jun 2025 | Second Action Scorecards | Comparable to 2023; 93 questions; 5,000+ volunteer hours cited for an earlier marking phase; 76% of councils used the 2025 right of reply |

CE UK has described itself as three staff plus volunteers. FOI Fest talk: ~400 councils, thousands of FOI questions, ~50 residents trained to process replies, ~700 volunteer hours on FOI capture alone in one cycle; 250+ volunteers across the Scorecards.

**Manual period before a public query interface.** **2019–2020/21**: declaration list and spreadsheets, public as a website but not a scored, comparable dataset. **~2–3 years** from “we collect the PDFs” to “we publish a score for every council.”

**Idea → first public version.** 2018–19 wave of council declarations → 2019 collection site (months). Collection site → CAPE 2020 → Plan Scorecards January 2022 (~2.5 years from founding site to first scored product).

**First public version → institutional recognition.** Councils using Scorecards in their own environment papers (Colchester case study, mySociety 2025); residents putting questions at full council; FT story pulled from the FOI dataset (mySociety, 27 Sept 2023). “Over 1 in 5 councils” using Scorecards internally is CE UK / mySociety’s own figure (prompt 38). That is self-reported uptake, not a select-committee citation. Log the distinction.

**Sources**

- Where did we come from and where are we going? — Climate Emergency UK. 2019 declaration site; mySociety approach in 2020. <https://climateemergency.uk/where-did-we-come-from-and-where-are-we-going/>
- About — Council Climate Scorecards. Plan Scorecards Jan 2022; Action Scorecards Oct 2023; 5,000 volunteer hours first marking phase. <https://councilclimatescorecards.uk/about/>
- CAPE — re3data. Started 2020-09-03. <https://www.re3data.org/repository/r3d100013972>
- Lightning Talk: Climate Action Plans Explorer — mySociety / Zarino, 2022. “Hand-updated Google Spreadsheets.” <https://www.youtube.com/watch?v=XRj1GbsrBqU>
- CE UK and mySociety are using people power and FOI — mySociety, 27 September 2023. WDTK Projects; 15 FOI volunteers plus 200 wider markers; right of reply. <https://www.mysociety.org/2023/09/27/ce-uk-and-mysociety-are-using-people-power-and-freedom-of-information-to-bring-transparency-to-local-climate-action/>
- Scorecards methodology — FOI via WDTK Jan–Feb 2023; 215 volunteers on 2023 first mark. <https://councilclimatescorecards.uk/2023/methodology/>
- Why are we using FOI requests? — Climate Emergency UK. Three staff; WDTK bulk; volunteer marking. <https://climateemergency.uk/scorecards-methodology-blog-series-why-are-we-using-foi-requests/>

---

## 40.5 Full Fact — fact-check site first, tools later

**Actual v1.** A fact-checking *website*, launched **2010**, after incorporation **29 July 2009** (first as Factcheck, renamed Full Fact). Idea from a 2008 conversation; Will Moy then a researcher for Lord Low; Michael Samuel the co-founder and funder. Initial money: Samuel donation plus Joseph Rowntree Charitable Trust Power and Accountability grant. First output is individual checked claims with sources, not a queryable policy-vs-spend register.

**Manual period.** The work *is* manual editorial. There was no multi-year private corpus that later grew a public UI. The public site *is* the product.

**Jump triggers later.** Charity status refused 2009, tribunal rejected 2011 (“civic engagement” too political), granted **2014** after objects rewritten to “advancement of public education.” Full Fact Finder (a journalist source-locator, five topics) launched **August 2013**. IFCN certification March 2017. Automated claim-matching came after a decade of editorial process. 2016 Moy remark: Full Fact began as a three-person operation.

**Idea → first public version.** 2008 conversation → 2010 site (~2 years).

**First public version → institutional recognition.** Charitable status 2014 (four years). IFCN 2017 (seven years). Parliamentary and media citation is continuous after that; no single “first select committee” date isolated on this pass.

**Sources**

- Who we are / Our history — Full Fact. Founded 2009, launched 2010; charity 2014. <https://fullfact.org/about/>
- Frequently asked questions — Full Fact. 2008 pub conversation; JRCT grant; cross-party trustees 2010. <https://fullfact.org/about/frequently-asked-questions/>
- Full Fact — Wikipedia. Charity refusal 2009–11; grant 2014; IFCN March 2017. <https://en.wikipedia.org/wiki/Full_Fact>
- Full Fact launches online fact-finding tool — Journalism.co.uk, 14 August 2013. <https://www.journalism.co.uk/full-fact-launches-online-fact-finder-for-journalists/>
- Companies House 06975984. Incorporated 29 July 2009; name changes 2011. <https://find-and-update.company-information.service.gov.uk/company/06975984/filing-history?page=4>

---

## 40.6 Institute for Government trackers — reports, not platforms

**Actual v1.** A **PDF report plus underlying datasets**, published by an already-recognised think tank.

- **Performance Tracker** first edition **Spring 2017**, with CIPFA. Five services (hospitals, adult social care, police, prisons, schools). Authors state it is “the first independent analysis of its kind” and “only the starting point.” Autumn 2017 expanded to ~100 datasets and nine services. Still an annual report series in 2025, not a public query UI over live rows.
- **Whitehall Monitor** is older. The 2025 edition is described as the 12th, which puts the first around **2013–14**. Same form: annual data-led assessment, not a citizen-facing search box.

**Manual period.** The “manual” work is the researchers’ spreadsheet. It never needed to become a public filer because IfG already had the distribution channel (launch events, journalists, officials).

**What triggered the jump.** There was no jump from personal tool to public interface. The institution existed; the tracker is a product line.

**Idea → first public version.** Not independently dated on this pass beyond “first edition Spring 2017.”

**First public version → institutional recognition.** Immediate, because the publisher was already citable. That is not a path a solo or three-person Deaf-sector project can copy.

**Sources**

- Performance Tracker: Spring 2017 — Institute for Government, 25 February 2017. <https://www.instituteforgovernment.org.uk/publication/report/performance-tracker-spring-2017>
- The politics of performance — Emily Andrews, IfG, 2 March 2017. “Only the starting point”; difficulty building a consistent spend time-series. <https://www.instituteforgovernment.org.uk/article/comment/politics-performance>
- Whitehall Monitor 2025 foreword — 12th edition. <https://www.instituteforgovernment.org.uk/publication/whitehall-monitor-2025/foreword>
- Trackers index — IfG. <https://www.instituteforgovernment.org.uk/our-work/trackers>

---

## 40.7 What happened when a tool skipped the narrow first job

The brief asked for tools that “tried to go straight to a public query interface without that intermediate stage.” Two different things get lumped under that sentence. They need separating.

**A. Public on day one, but the user *creates* the record — these scaled.**  
FixMyStreet and WhatDoTheyKnow. No pre-built national dataset. The interface *is* the collection method. That design only transfers to this project if the first public action is “file an FOI / log a sourced row,” not “query the finished gap register.”

**B. Public on day one as a general civic platform — these drifted or closed.**

**PledgeBank.** Announced November 2004, launched **13 June 2005**, closed **2015**. Second official mySociety project after WriteToThem. “I’ll do X if N other people will.” Translated into 14 languages. Real outcomes (Open Rights Group was founded via a pledge). Closed because the concept was “too diffuse,” marketing was thin, Groupon/Kickstarter occupied the same mechanic, and a small organisation chose to concentrate on core sites. Ten-year run, then a deliberate shutdown — not a crash on launch day.

**ReportEmptyHomes (2008).** FixMyStreet codebase reused for empty-property reports, partnered with the Empty Homes Agency. Channel 4 *Great British Property Scandal* (2011) produced 7,900 reports and award nominations. It did not become a standing mySociety pillar. Partner-campaign tools follow the campaign.

**MIT Promise Tracker** (prompt 38). Public campaigns from 2015; project marked ended December 2018; GitHub archived January 2022. Lab-cycle sunset.

**Lesson that is actually documented.** Failure in this set is usually *loss of focus or host*, not “we launched a website before the data model was perfect.” PledgeBank launched as a public interface and worked; it died when the organisation would not make it the main job. A BSL gap monitor that tries to be a general Deaf civic platform on day one inherits that death.

**Sources**

- The story of Pledgebank — mySociety, 24 February 2015. Announced Nov 2004; launched 13 June 2005. <https://www.mysociety.org/2015/02/24/the-story-of-pledgebank/>
- Discontinued civic tech conference — SocietyWorks, 28 November 2024. Closed 2015 to concentrate; concept too diffuse. <https://www.societyworks.org/2024/11/28/discontinued-civic-tech-conference/>
- Learning from the civic tech graveyard — Civic Tech Field Guide, 10 January 2019. PledgeBank and OpenCongress closed because the parent chose another priority. <https://civictech.guide/learning-from-the-civic-tech-graveyard/>
- Case Study: EmptyHomes — mySociety. 2008 site; 2011 TV tie-in; 7,900 reports. <https://www.mysociety.org/community/case-study-emptyhomes/>

---

## 40.8 Timeframes in one place

Figures below are what the sources actually say. Where a source is vague, it stays vague.

| Tool | Idea / spark | First thing that existed | First public version | Jump trigger | Institutional recognition |
|---|---|---|---|---|---|
| Public Whip | 18 Mar 2003 Iraq division | Two-person Hansard parser | Summer 2003 site | Spare-time build | New Statesman New Media Award 2004 |
| TheyWorkForYou | Same circle, ~2003 | Volunteer website on that parser | 6 Jun 2004 | mySociety adoption early 2006; DCA API summer 2006 | Channel 4 2005; Lords praise mid-2000s; Escher report 2011 |
| WhatDoTheyKnow | 2006 idea competition | Funded 18-month build | 22 Feb 2008 (thin) | JRRT grant + competition | Awards 2008; Justice Committee evidence Feb 2012 |
| FixMyStreet | Phone-box anecdote + DCA grant | Beta map site | 2 Feb 2007 first report; Mar 2007 launch | £10k innovations grant | *Times* Apr 2007; councils later white-label the code |
| CE UK → Scorecards | 2018–19 declaration wave | 2019 collection website + sheets | CAPE 2020; Plan Scorecards Jan 2022 | mySociety partnership 2020 | Council uptake; press from FOI dataset 2023 |
| Full Fact | 2008 conversation | Editorial fact-check site | 2010 | Founder money + JRCT | Charity 2014; IFCN 2017 |
| IfG Performance Tracker | Think-tank product line | Researchers’ datasets | Spring 2017 report | Already-citable host | Immediate |
| PledgeBank | Nov 2004 announcement | Public pledge site | 13 Jun 2005 | mySociety project #2 | Closed 2015 (focus, not launch failure) |

**Ranges a solo or small team can honestly quote**

- Parser / collection to first *public page*: **months** (Public Whip, FixMyStreet beta) to **~18 months** (WhatDoTheyKnow funded build).
- Collection website to *scored, comparable, all-bodies product*: **about 2–3 years** (CE UK 2019 → Plan Scorecards Jan 2022).
- Public version to a *parliamentary evidence slot*: **about 4 years** in the one clean case (WhatDoTheyKnow 2008 → Justice Committee 2012). TheyWorkForYou was reused by a broadcaster within a year, which is faster, but that was an election product on already-parsed Hansard — not a new dataset.
- Volunteer hours on a national score: CE UK cites **5,000+** for one marking phase and **~700** on FOI capture in another cycle. That is the labour cost of pattern 1, not the software cost.

---

## 40.9 What this means for the tool in this dossier

Do not copy FixMyStreet’s “ship the filer and the data will appear.” BSL / AIS / spend rows do not appear when a user clicks a map. They appear when someone reads a PDF, an FOI reply or a contract notice and writes a cited cell. That is the Climate Scorecards / Public Whip pattern.

The dossier is already past idea-stage:

- A geographically bounded gold-standard series exists (SWL 878, Oct 2024–Jun 2025).
- An FOI companion log and templates exist.
- AIS, DWP, Jobcentre and EOL briefs exist as sourced markdown.

The documented next step in the cousins is **not** a public query API. It is either:

1. keep the collection public as a static briefing / spreadsheet / CAPE-style explorer, then score once the question set is stable, or
2. use WhatDoTheyKnow (already the FOI pipe) as the collection interface and treat the “platform” as a later publication of marked rows, with a right of reply.

The documented way to kill it is to skip that and launch a general “Deaf civic platform” whose job is everything PledgeBank’s job was: too diffuse for a small team to maintain.

Prompt 41 should take the hour/year ranges above and not invent tighter ones. Prompt 43 should take CE UK’s WDTK-at-400-councils practice as the FOI-at-scale precedent.

---

## 40.10 Search log

Checked 8–9 September 2026: mySociety history, launch and anniversary posts; Escher 2011; GovLab TheyWorkForYou case; Public Whip FAQ; WDTK timeline; FixMyStreet birthday / million / *Times* 2007; CE UK about / origin / methodology / FOI blog; CAPE re3data; Full Fact about / FAQ / CH filing; IfG Performance Tracker 2017 and Whitehall Monitor 2025; PledgeBank retrospectives and civic-tech graveyard.

**Gaps.** No founder interview was found that gives a week-count for the Public Whip parser. No select-committee *report* was isolated that cites Climate Scorecards as evidence (council and press use are documented; parliamentary citation is not, on this pass). Full Fact’s first URL and first published check were not retrieved as scans. Those remain gaps.
