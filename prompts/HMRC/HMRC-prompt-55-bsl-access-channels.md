# Prompt 55 — Current, verified state of HMRC's BSL/Deaf access channels

**Master index prompt 55.** First file in the HMRC and BSL/Deaf access batch (prompts 55–61). Compiled 9 September 2026. Dossier rule: stay unbiased; follow money and fulfilment; do not wear a DEI or anti-DEI banner. An unsourced AI claim is the lowest tier. Gaps are logged as gaps, not filled guesses.

**What this prompt is for.** Close the first-pass currency gaps on HMRC's live BSL video-relay supplier, the RAD partnership / microsite, whether either is still a "pilot", and the current Relay UK / textphone numbers on the main HMRC helplines. Nothing in prompts 56–61 should be built on a stale SignVideo vs InterpretersLive assumption.

**Index check.** `SuperGrok_Research_Prompt_Pack.md` already lists 55–61 and sets **NEXT PROMPT NUMBER TO USE: 62**. This file is the research answer to prompt 55, not a new numbered batch.

---

## Headline

HMRC's own extra-support guide, live in HTML on 9 September 2026, names **SignVideo** as the BSL video-interpreter supplier and publishes two working one-click hosts:

- Extra Support: `https://hmrcextrasupport.signvideo.net/`
- Debt Management: `https://hmrcdebtmanagement.signvideo.net/`

Both hosts returned HTTP 302 to SignVideo's live WebRTC one-click-call service on the same day. InterpretersLive! (Sign Solutions) is **not** named on that GOV.UK page. It still appears on LITRG's additional-needs guide (updated 29 July 2026) and on a 2023 InterpretersLive directory page for Working Tax Credits. Treat InterpretersLive as a **stale or residual third-party listing**, not as HMRC's current published VRS.

The 2015 HMRC–RAD "pilot" news story was withdrawn on 13 December 2022 with the line that the pilot **ended in 2022** and that a BSL service is now "embedded" in extra support. The old joint microsite `royaldeaftax.org.uk` is not a working public site. The live RAD product is RAD's own pages under `royaldeaf.org.uk/partner/hmrc-service-support/`, booked via Calendly, still promoted by HMRC on X on 9 May 2026 (Deaf Awareness Week) and still listed on HMRC's VCS-grant page. It is not described as a pilot on current HMRC or RAD pages. RAD's own pages disagree with each other on whether face-to-face London appointments still exist.

Relay UK is the general text path: dial **18001** then the published helpline number. Dedicated textphones exist for some lines (Income Tax / Self Assessment complaints, National Insurance, VAT/customs complaints, employers' complaints) and are **not** published on every general-enquiry page, including Self Assessment general enquiries and payment-problems / debt lines.

---

## 55.1 Video-relay supplier — SignVideo today, InterpretersLive residual

HMRC's extra-support guide, section "If you use British Sign Language (BSL)":

> You can contact HMRC using a BSL video interpreter from the SignVideo service:

The same HTML block contains two outbound links and no InterpretersLive URL:

| Published label on GOV.UK | Live URL | What a HEAD request returned on 9 Sep 2026 |
|---|---|---|
| HMRC Extra Support (SignVideo) | https://hmrcextrasupport.signvideo.net/ | HTTP 302 to `service.signvideo.uk/webrtc/#/oneclickcall` with destination `hmrc1@signvideo.uk` |
| HMRC Debt Management (SignVideo) | https://hmrcdebtmanagement.signvideo.net/ | HTTP 302 to the same WebRTC host with destination `hmrc2@signvideo.uk` |

Source: Get help from HMRC if you need extra support — If you cannot use a telephone and need a different way to contact HMRC, GOV.UK. First published 15 July 2014. Internal `govuk:updated-at` 9 September 2026 16:05 BST. Displayed `govuk:public-updated-at` still 18 November 2014 — the public "last updated" stamp has not been bumped even though the SignVideo hosts are in the live HTML.  
https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact  
Printable copy of the same guide (SignVideo wording also present on this pass):  
https://www.gov.uk/get-help-hmrc-extra-support/print

SignVideo's own public SignDirectory lists two matching organisation names, "HMRC Extra Support" and "HMRC Debt Management", in the same directory that also lists Companies House.  
https://signvideo.co.uk/sign-directory/

HMRC does **not** publish a SignVideo connect button for Income Tax general enquiries, Self Assessment, VAT, PAYE for employers, or tax credits as separate one-click hosts. The two published hosts are Extra Support and Debt Management only. A BSL user who needs a specific tax line is expected either to use Extra Support SignVideo and ask to be routed, use Relay UK / textphone on the numbered helpline, or go through RAD. That routing is an inference from the published map, not a published HMRC instruction — flag it as such.

### InterpretersLive — still cited, not on the live HMRC page

LITRG "Getting tax help if you have additional needs", updated 29 July 2026, still says:

> You can contact HMRC via a BSL video interpreter service. There is more information on the InterpretersLive website.

LITRG link target: https://www.interpreterslive.co.uk/app/hmrc/  
That URL returned HTTP 401 to an unauthenticated fetch on 9 September 2026 (bot/WAF gate, not a clean 404).  
https://www.litrg.org.uk/tax-nic/getting-help-hub/getting-tax-help-if-you-have-additional-needs

InterpretersLive still publishes a directory entry "HMRC – Working Tax Credits", page dated 27 June 2023, claiming on-demand BSL 7 days a week 08:00–00:00 via Sign Solutions. Same 401 on direct fetch this pass; the listing is indexed by search engines. Working Tax Credits is a closed-to-new-claims legacy benefit, so even if the connect button still works for a human browser, it is not a general HMRC access channel.  
https://www.interpreterslive.co.uk/directory/hmrc-working-tax-credits/

**Currency finding.** First-pass notes that named both SignVideo hosts *and* InterpretersLive as current HMRC suppliers are half-right. Official HMRC copy on 9 September 2026 is SignVideo only. InterpretersLive remains in LITRG and in its own 2023 tax-credits listing. Do not write "HMRC uses InterpretersLive" without naming LITRG as the source and dating it.

---

## 55.2 RAD partnership and the old joint microsite

### What ended

HMRC news story "New services available for HMRC's deaf customers", published 29 June 2015, withdrawn 13 December 2022:

> The pilot scheme announced in this news story between HMRC and the Royal Association for Deaf People (RAD) ended in 2022. A British Sign Language service is now embedded as part of HMRC's wide range of help and assistance for customers who need extra support.

The withdrawn story described (a) webcam video relay with a BSL interpreter talking to an HMRC adviser and (b) a RAD Advocacy and Advice service, both bookable through a "joint HMRC / RAD Tax Help Centre".  
https://www.gov.uk/government/news/new-services-available-for-hmrcs-deaf-customers

The 2016 RAD press-release video still names the old URL `www.royaldeaftax.org.uk` as the BSL tax-information site. HEAD requests to `https://www.royaldeaftax.org.uk/` and `http://royaldeaftax.org.uk/` on 9 September 2026 returned **405 Not Allowed**, not a working content page. Treat the joint microsite as **gone / not re-confirmable as a live public site**.  
https://www.youtube.com/watch?v=-SEqBzAK88E (RAD, 1 December 2016)

### What is live now

RAD's current HMRC service page:

https://royaldeaf.org.uk/partner/hmrc-service-support/

RAD describes a partnership with HMRC, free independent confidential support UK-wide (explicitly including Scotland, Wales and Northern Ireland), BSL translation of HMRC letters, and help with Self Assessment, Child Benefit, Marriage Allowance, PAYE "and much more". Remote appointments are booked through Calendly:

https://calendly.com/tax-advocacy-service/30min

Calendly title on a mid-2026 snapshot: "HMRC Tax advice – 30 minutes", "specialist service for deaf individuals who use British Sign Language (BSL) or need deaf-accessible communication", "free, confidential advice and support with HMRC matters such as tax, benefits, and self-employment", "exclusively for deaf individuals only".

Face-to-face: the same partner page says appointments at RAD's London office, booked by emailing enquiries@royaldeaf.org.uk. A later how-to page and a 25 June 2025 RAD YouTube video say the national service is **"remote only"**. That is an internal RAD contradiction, not a GOV.UK contradiction.  
How-to page (published 16 June 2025): https://royaldeaf.org.uk/how-to-book-an-appointment-to-get-help-with-hmrc/  
Booking video description still carrying the Calendly link: https://www.youtube.com/watch?v=4d6LKS1Wf4o

RAD also runs HMRC workshops. A listed face-to-face Self Assessment session at 36 Graham Street, London N1 8GJ on 21 May 2026 covered Self Assessment, Making Tax Digital, the HMRC app, and avoiding penalties. Contact given as email or BSL video to taxhelp@royaldeaf.org.uk.  
https://royaldeaf.org.uk/event-and-workshop/hmrc-self-assessment-face-to-face-21-may/

### HMRC still points at RAD, but not as a BSL-relay product

HMRC VCS extra-support list, public-updated 5 April 2024, still carries a RAD entry. The official blurb funds "welfare benefits, housing, debt support, health care access and advocacy, all in British Sign Language (BSL)". It does **not** say "BSL video relay into an HMRC helpline" and does **not** name SignVideo.  
https://www.gov.uk/guidance/voluntary-and-community-sector-organisations-who-can-give-you-extra-support

Charity Today, 23 September 2024: RAD used HMRC Voluntary and Community Sector Grant Funding (programme running since 2014) to set up an "HMRC Advice Team"; Operations Manager Sarah Watson; work includes BSL explanation of PAYE / P60 / tax-code vocabulary, letter translation, and screen-share form filling; "The team at RAD work closely with HMRC's Extra Support Team".  
https://www.charitytoday.co.uk/hmrc-celebrates-royal-association-for-deaf-peoples-support-for-deaf-taxpayers/

HMRC official X account @HMRCgovuk, 9 May 2026, Deaf Awareness Week:

> Did you know we have a partnership with @royaldeaf to offer free, accessible tax support, including BSL help and one to one guidance.

That is the most recent HMRC-origin confirmation found that the partnership is still treated as current.  
https://x.com/HMRCgovuk/status/2053188109341180029

LITRG additional-needs page (29 July 2026) also still points readers to RAD videos and workshops.

**Pilot vs permanent.** Current HMRC extra-support pages do not use the word "pilot" for SignVideo or for RAD. The only official "pilot" language found is on the withdrawn 2015 news story, which states the pilot ended in 2022. No end-date for the current RAD VCS-funded advice service was found on GOV.UK or on RAD's live pages. Grant-funded VCS arrangements can still lapse when a grant round ends — that is a funding-status gap, not evidence that the service has already closed.

---

## 55.3 HMRC Charter and extra-support principles — BSL is not named

The HMRC Charter (legal duty under the Commissioners for Revenue and Customs Act 2005) last updated 30 July 2024. Relevant standards: "Being aware of your personal situation" and "Recognising that someone can represent you". No BSL, SignVideo, or Deaf-specific sentence.  
https://www.gov.uk/government/publications/hmrc-charter/the-hmrc-charter  
https://www.gov.uk/government/publications/hmrc-charter

"HMRC's principles of support for customers who need extra help", same 30 July 2024 update. Commits to monitoring calls and post to identify customers who need extra help, including disability; advisers transfer those calls to the Extra Support Team; names "sensory disabilities, like a visual, hearing or speech impairment" as an example group on the extra-support guide. Does not name BSL or a video-relay supplier. Tax charities "will be able to provide independent advice".  
https://www.gov.uk/government/publications/hmrc-charter/hmrcs-principles-of-support-for-customers-who-need-extra-help--3

---

## 55.4 Relay UK and textphone numbers, by major helpline

HMRC's extra-support page states the general rule:

> Dial 18001 then the relevant contact number to use the Relay UK Text Service.

Worked example on that page: Income Tax general enquiries 0300 200 3300 → **18001 0300 200 3300**.  
It then points to a filtered contact list "textphone service for some of its helplines". Dedicated textphones are therefore **not universal**.

Checked against the live contact pages on 9 September 2026:

| Helpline | Voice number | Relay UK (18001 + voice) | Dedicated textphone on that page or on the complaints page | Notes |
|---|---|---|---|---|
| Income Tax general enquiries | 0300 200 3300 | Yes — page tells you to dial 18001 then 0300 200 3300 | 0300 200 3319 on the complaints page (Income Tax *and* Self Assessment complaints share this textphone) | General-enquiry page itself did not print a textphone in this pass |
| Self Assessment general enquiries | 0300 200 3310 | Not printed on the SA general page in this pass | 0300 200 3319 on the complaints page | SA page pushes digital assistant / webchat first. Public-updated 28 July 2026 |
| VAT / customs / international trade | 0300 200 3700 | Yes — 18001 then 0300 200 3700 | 0300 200 3719 on the complaints page and on imports/exports enquiries | Same textphone used for some customs lines |
| PAYE / employers | 0300 200 3200 | Not printed on the employer-enquiries page in this pass | 0300 200 3212 on the complaints page | Employer page public-updated 19 December 2025 |
| Tax credits | 0300 322 9129 | Yes — 18001 then 0300 322 9129 | No dedicated textphone found on the live tax-credits enquiries page | Number has moved off the old 0345 range. Page public-updated 22 May 2026; internal update 4 Sep 2026 |
| Debt / payment problems | SA 0300 200 3820; VAT 0300 200 3831; PAYE 0300 200 3819; CT 0300 200 3840 | Not printed on the payment-problems page in this pass | No dedicated textphone found on that page | BSL path published separately via SignVideo Debt Management host. Page public-updated 19 December 2025 |
| National Insurance (comparator, not asked but has a clean textphone) | 0300 200 3500 | Yes — 18001 then 0300 200 3500 | 0300 200 3519 | Clean three-channel example |
| Extra Support Team webchat | n/a (webchat) | n/a | n/a | Opening times on Extra Support Team contact page: Mon–Fri 08:00–19:30, Sat 08:00–16:00. Page published 14 May 2025, last updated 24 November 2025 |

Sources for the table:

- Extra support alternative-contact page (Relay rule + Income Tax example): https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact
- Income Tax enquiries: https://www.gov.uk/find-hmrc-contacts/income-tax-enquiries
- Self Assessment: https://www.gov.uk/find-hmrc-contacts/self-assessment-general-enquiries and https://www.gov.uk/government/organisations/hm-revenue-customs/contact/self-assessment
- VAT: https://www.gov.uk/government/organisations/hm-revenue-customs/contact/vat-enquiries
- Employers: https://www.gov.uk/government/organisations/hm-revenue-customs/contact/employer-enquiries
- Tax credits: https://www.gov.uk/government/organisations/hm-revenue-customs/contact/tax-credits-enquiries
- Payment problems: https://www.gov.uk/find-hmrc-contacts/payment-problems-enquiries
- Complaints page (the textphone cluster): https://www.gov.uk/government/organisations/hm-revenue-customs/contact/complain-about-hmrc
- Extra Support Team contact: https://www.gov.uk/find-hmrc-contacts/extra-support-team
- National Insurance: https://www.gov.uk/find-hmrc-contacts/national-insurance-enquiries
- Relay UK how-to: https://www.relayuk.bt.com/

**Thin spots, not guesses.** No published textphone was found on the Self Assessment *general* page, the employer *general* page, or the payment-problems page. Those lines still have a complaints-page textphone or a Relay-prefix option in principle (18001 + the voice number works on any UK number that accepts it), but HMRC has not written that instruction on those particular pages. Debt has a SignVideo host instead of a published textphone.

---

## 55.5 What a first-pass brief should now treat as stale

| First-pass claim | Status on 9 Sep 2026 |
|---|---|
| `hmrcextrasupport.signvideo.net` and `hmrcdebtmanagement.signvideo.net` are live HMRC SignVideo hosts | **Re-confirmed.** Both 302 to SignVideo WebRTC. Named on the live extra-support guide |
| HMRC also uses InterpretersLive for general extra support | **Not on the live HMRC page.** Survives on LITRG (29 Jul 2026) and a 2023 InterpretersLive Working Tax Credits listing |
| Joint HMRC/RAD microsite `royaldeaftax.org.uk` is the booking/info site | **Not re-confirmable as a live public site** (405). Replaced by `royaldeaf.org.uk/partner/hmrc-service-support/` + Calendly |
| HMRC–RAD BSL service is a "pilot" | **Officially ended 2022** per the withdrawn 2015 news story. Current pages do not use "pilot" and do not print an end date |
| RAD webcam appointment is a three-way call into an HMRC adviser | **Not how RAD now describes the service.** Current RAD copy is RAD's own BSL tax adviser / letter translation / workshops, which then "work closely with" Extra Support. The three-way webcam-into-HMRC product is what SignVideo Extra Support / Debt Management now is |

---

## Findings table

| Label | Value | Source name | Source URL | Publication date | Confidence (Verified/Contested/No reliable figure found) |
|---|---|---|---|---|---|
| Current HMRC-published BSL VRS supplier | SignVideo | Get help from HMRC if you need extra support (cannot use telephone) | https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact | First published 15 Jul 2014; HTML `updated-at` 9 Sep 2026; public-updated stamp still 18 Nov 2014 | Verified |
| SignVideo Extra Support one-click host | https://hmrcextrasupport.signvideo.net/ (302 to SignVideo WebRTC, dest `hmrc1@signvideo.uk`) | Same GOV.UK page; live HEAD check 9 Sep 2026 | https://hmrcextrasupport.signvideo.net/ | Link live 9 Sep 2026 | Verified |
| SignVideo Debt Management one-click host | https://hmrcdebtmanagement.signvideo.net/ (302 to SignVideo WebRTC, dest `hmrc2@signvideo.uk`) | Same GOV.UK page; live HEAD check 9 Sep 2026 | https://hmrcdebtmanagement.signvideo.net/ | Link live 9 Sep 2026 | Verified |
| SignVideo directory lists the same two HMRC services | "HMRC Extra Support" and "HMRC Debt Management" appear in SignDirectory | SignVideo SignDirectory | https://signvideo.co.uk/sign-directory/ | Directory page dated 20 Aug 2021; entries current on this pass | Verified |
| InterpretersLive named as HMRC BSL route on GOV.UK extra-support page | Not named. Official copy is SignVideo only | Same GOV.UK extra-support page | https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact | 9 Sep 2026 HTML | Verified (absence on that page) |
| InterpretersLive still cited by LITRG | Yes — "more information on the InterpretersLive website", link `/app/hmrc/` | LITRG, Getting tax help if you have additional needs | https://www.litrg.org.uk/tax-nic/getting-help-hub/getting-tax-help-if-you-have-additional-needs | Updated 29 Jul 2026 | Verified as LITRG wording; Contested as a description of HMRC's current published channel |
| InterpretersLive HMRC Working Tax Credits listing | Directory page still indexed; on-demand 08:00–00:00 7 days; Sign Solutions | InterpretersLive directory | https://www.interpreterslive.co.uk/directory/hmrc-working-tax-credits/ | Page dated 27 Jun 2023; HTTP 401 to bot fetch 9 Sep 2026 | Contested (page exists in search index; live connect not re-confirmed) |
| SignVideo / InterpretersLive coverage of Income Tax, SA, VAT, PAYE, tax credits as separate one-click hosts | No separate hosts published on GOV.UK beyond Extra Support and Debt Management | Extra-support guide + contact pages checked this pass | https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact | 9 Sep 2026 | Verified as unpublished; routing via Extra Support is an inference |
| 2015 HMRC–RAD BSL pilot status | Pilot ended 2022; BSL now "embedded" in extra support | Withdrawn HMRC news story | https://www.gov.uk/government/news/new-services-available-for-hmrcs-deaf-customers | Published 29 Jun 2015; withdrawn 13 Dec 2022 | Verified |
| Old joint microsite royaldeaftax.org.uk | Not a working public site (405). Named in 2016 RAD press video | RAD YouTube 1 Dec 2016; HEAD check 9 Sep 2026 | https://www.youtube.com/watch?v=-SEqBzAK88E | Video 2016; host dead on this pass | Verified (absence) |
| Current RAD HMRC service URL | https://royaldeaf.org.uk/partner/hmrc-service-support/ | RAD, HMRC Service Support | https://royaldeaf.org.uk/partner/hmrc-service-support/ | RAD page dated 30 Dec 2024 in search index; content live 9 Sep 2026 | Verified |
| Current RAD booking URL | Calendly 30-min "HMRC Tax advice" slot, deaf-only | RAD booking video + Calendly | https://calendly.com/tax-advocacy-service/30min | Video published 25 Jun 2025; Calendly live through 2026 | Verified |
| RAD remote vs face-to-face | Partner page offers both (F2F London via enquiries@royaldeaf.org.uk). How-to page and Jun 2025 video say national service is "remote only". Workshops still listed F2F in London May 2026 | RAD partner page; how-to page; workshop page | https://royaldeaf.org.uk/partner/hmrc-service-support/ ; https://royaldeaf.org.uk/how-to-book-an-appointment-to-get-help-with-hmrc/ ; https://royaldeaf.org.uk/event-and-workshop/hmrc-self-assessment-face-to-face-21-may/ | 2024–2026 | Contested (RAD pages disagree) |
| Is the current RAD/HMRC service described as a pilot with an end date? | No. Current HMRC and RAD pages do not use "pilot" and print no end date. VCS grant page last *public*-updated 5 Apr 2024 | Extra-support guide; RAD partner page; VCS list; withdrawn 2015 story | https://www.gov.uk/guidance/voluntary-and-community-sector-organisations-who-can-give-you-extra-support | VCS public-updated 5 Apr 2024 | Verified for current wording; grant-round end date not found |
| Most recent HMRC-origin confirmation of the RAD partnership | @HMRCgovuk Deaf Awareness Week post | HMRC official X | https://x.com/HMRCgovuk/status/2053188109341180029 | 9 May 2026 | Verified |
| RAD funded by HMRC VCS grant / works with Extra Support Team | Charity Today write-up of HMRC celebrating RAD's HMRC Advice Team; VCS list still carries RAD | Charity Today; GOV.UK VCS list | https://www.charitytoday.co.uk/hmrc-celebrates-royal-association-for-deaf-peoples-support-for-deaf-taxpayers/ | 23 Sep 2024 | Verified as contemporaneous reporting; grant amount for the current year not published there |
| HMRC Charter / extra-help principles name BSL? | No. Charter names "personal situation" and representation. Principles name Extra Support Team transfer and "hearing or speech impairment" | HMRC Charter; principles of support | https://www.gov.uk/government/publications/hmrc-charter/the-hmrc-charter | Last updated 30 Jul 2024 | Verified (absence of BSL wording) |
| Relay UK general rule for HMRC | Dial 18001 then the relevant contact number. Worked example: 18001 0300 200 3300 for Income Tax | Extra-support alternative-contact page | https://www.gov.uk/get-help-hmrc-extra-support/cannot-use-telephone-different-way-to-contact | HTML live 9 Sep 2026 | Verified |
| Income Tax voice + Relay + textphone | Voice 0300 200 3300; Relay 18001 0300 200 3300; textphone 0300 200 3319 (complaints page) | Income Tax contact; complaints page | https://www.gov.uk/find-hmrc-contacts/income-tax-enquiries ; https://www.gov.uk/government/organisations/hm-revenue-customs/contact/complain-about-hmrc | Contact page public-updated 19 Dec 2025 | Verified |
| Self Assessment voice + text access | Voice 0300 200 3310. No Relay/textphone printed on the general SA page. Complaints page textphone 0300 200 3319 | SA contact; complaints page | https://www.gov.uk/find-hmrc-contacts/self-assessment-general-enquiries | Public-updated 28 Jul 2026 | Verified (gap on the general page) |
| VAT voice + Relay + textphone | Voice 0300 200 3700; Relay 18001 0300 200 3700; textphone 0300 200 3719 (complaints / customs pages) | VAT enquiries; complaints page | https://www.gov.uk/government/organisations/hm-revenue-customs/contact/vat-enquiries | Public-updated 15 Jul 2026 | Verified |
| PAYE / employers voice + textphone | Voice 0300 200 3200. No Relay printed on employer-enquiries page. Complaints page textphone 0300 200 3212 | Employer enquiries; complaints page | https://www.gov.uk/government/organisations/hm-revenue-customs/contact/employer-enquiries | Public-updated 19 Dec 2025 | Verified (gap on the general page) |
| Tax credits voice + Relay | Voice 0300 322 9129; Relay 18001 0300 322 9129. No dedicated textphone found on that page | Tax credits enquiries | https://www.gov.uk/government/organisations/hm-revenue-customs/contact/tax-credits-enquiries | Public-updated 22 May 2026 | Verified |
| Debt / payment-problems textphone | No dedicated textphone printed on the payment-problems page. Four voice numbers for SA/VAT/PAYE/CT payment problems. BSL path is the SignVideo Debt Management host | Payment problems contact; extra-support SignVideo link | https://www.gov.uk/find-hmrc-contacts/payment-problems-enquiries | Public-updated 19 Dec 2025 | Verified (absence of textphone on that page) |
| Extra Support Team webchat hours | Mon–Fri 08:00–19:30; Sat 08:00–16:00; closed bank holidays | Extra Support Team contact page | https://www.gov.uk/find-hmrc-contacts/extra-support-team | Published 14 May 2025; last updated 24 Nov 2025 | Verified |

---

## Confidence and gaps for the rest of the batch

- **Use SignVideo Extra Support and SignVideo Debt Management as the current official HMRC BSL video channels.** Do not write InterpretersLive as HMRC's live published supplier without attributing that to LITRG (July 2026) and dating it.
- **Use RAD's royaldeaf.org.uk partner page + Calendly, not royaldeaftax.org.uk.** The joint microsite is not live.
- **Do not call the current arrangement a pilot.** The pilot language is confined to a withdrawn 2015 story that itself says the pilot ended in 2022.
- **RAD is advice/translation/workshops in BSL, plus a working relationship with Extra Support — it is not the same product as SignVideo one-click into HMRC.** Prompt 56 should treat those as two routes, not one.
- Unpublished: whether a SignVideo Extra Support interpreter can actually transfer into a named tax helpline; whether InterpretersLive Working Tax Credits still connects for a human user; current-year VCS grant value to RAD; whether F2F London RAD tax appointments are still offered.
- HMRC extra-support guide's public "last updated" stamp (18 Nov 2014) is stale relative to the 9 Sep 2026 HTML. Quote the live URLs, not the displayed date, when citing the SignVideo hosts.
