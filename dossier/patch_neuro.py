content = open("bsl_dossier.html", encoding="utf-8").read()

start = content.index("id:'nhs-interpreter'")
rest = content[start:]
end_marker = rest.index("\n  { id:")
block = rest[:end_marker]
anchor = block[-350:]
assert content.count(anchor) == 1, "anchor found %d times" % content.count(anchor)

close_tail = "\n    ]},"
assert anchor.endswith(close_tail), repr(anchor[-30:])
prefix = anchor[:-len(close_tail)] + ","

figs = []
figs.append("      {label:'No official UK figure for autism/ADHD co-occurrence among Deaf BSL-users', value:'CRIDE additional-need rate (24% of deaf children) is the nearest published child statistic, and is not autism-split or BSL-split', source:'Project research pass, prompts 85-91 (Neurodivergence batch); CRIDE', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'No mandated combined Deaf+autism/ADHD diagnostic pathway exists', value:'Childhood assessment can go through National Deaf CAMHS; an adult BSL-led neurodevelopmental pathway remains a Locked Out policy ask, not a live NHS service', source:'Locked Out (BSL Advisory Board, 27 Nov 2025, GOV.UK); NDCS Deafness and autism (May 2025)', sourceUrl:'https://www.gov.uk/government/publications/bsl-user-experience-of-health-and-social-care-in-uk', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'NHS autism referral backlog (general population, no Deaf/BSL split)', value:'270,701 open suspected-autism referrals, March 2026; 89.7% (242,708) open 13+ weeks', source:'NHS Digital, Autism Statistics, April 2025 to March 2026 (published 14 May 2026)', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Locked Out additional-disabilities and autism-deafness overlap figures (30-40%; 3.5%)', value:'Cited in project research from the Locked Out report, but neither figure could be independently located in the fetched excerpt on two separate verification passes; treat as contested until the source PDF is opened directly, not via an automated fetch tool', source:'Locked Out (BSL Advisory Board, 27 Nov 2025, GOV.UK) -- figures as cited, not independently re-derived', sourceUrl:'https://www.gov.uk/government/publications/bsl-user-experience-of-health-and-social-care-in-uk', lastVerified:'2026-09-14', status:'contested'}")
figs.append("      {label:'AtW BSL Adjustments Planner and the Health Adjustment Passport are two separate tools under one grant', value:'One AtW grant, separate tariffs, one cap (GBP69,260, frozen to 31 Mar 2027); no published overlap count inside the 3,210 BSL-interpreter AtW customers, and no dual assessment protocol found', source:'Project research pass, prompt 87; AtW BSL Adjustments Planner (27 Nov 2024)', sourceUrl:'https://www.gov.uk/government/publications/access-to-work-bsl-adjustments-planner', lastVerified:'2026-09-14', status:'verified'}")

new_block = prefix + "\n" + ",\n".join(figs) + "\n    ]},"

content = content.replace(anchor, new_block, 1)
open("bsl_dossier.html", "w", encoding="utf-8").write(content)
print("done, new length:", len(content))
