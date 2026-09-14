content = open("bsl_dossier.html", encoding="utf-8").read()

start = content.index("id:'access-to-work'")
rest = content[start:]
end_marker = rest.index("\n  { id:")
block = rest[:end_marker]
anchor = block[-350:]
assert content.count(anchor) == 1, "anchor found %d times" % content.count(anchor)

close_tail = "\n  ]},"
assert anchor.endswith(close_tail), repr(anchor[-30:])
prefix = anchor[:-len(close_tail)] + ","

figs = []
figs.append("      {label:'Equality Act reasonable-adjustment duty applies at recruitment stage, before any job offer exists', value:'ss.20, 39 and 55 require an employer or recruitment agency to adjust the recruitment process for a disabled applicant -- including a BSL or DeafBlind interpreter at interview -- unless not reasonable on the facts; applies even to an unsuccessful candidate', source:'Equality Act 2010 ss.20, 39, 55; ACAS Following discrimination law - Recruitment and Interviewing job applicants', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Access to Work Communication Support at Interview (CSI) is a candidate-applied funding route, not a transfer of the employer duty', value:'Candidate (not employer) applies before the interview; 100% of approved costs, no cost-share, paid after the interview; does not move or discharge the Equality Act recruitment-stage duty', source:'GOV.UK, Apply for communication support at a job interview (spot-checked live 14 Sep 2026, holds verbatim; page last updated 8 Oct 2025)', sourceUrl:'https://www.gov.uk/guidance/apply-for-communication-support-at-a-job-interview-if-you-have-a-disability', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Pre-offer health questions are banned except for named exceptions, including asking whether an adjustment is needed for the recruitment process itself', value:'Equality Act s.60 bars general pre-offer health screening; asking if a candidate needs an adjustment for the interview/assessment itself is a permitted exception. Elite Careplus Ltd (EHRC, 2021) is the only concluded enforcement action found on this point, and is not a Deaf/BSL case.', source:'Equality Act 2010 s.60; EHRC employer and applicant s.60 guides; Elite Careplus Ltd investigation (EHRC, 2021)', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Illustrative tribunal case: employer failure to arrange an interview interpreter', value:'Murphy v Sheffield Hallam University (EAT/6/99, [1999] UKEAT 0006_19_1101, 11 Jan 2000) -- Disability Discrimination Act 1995 (not Equality Act 2010). University unlawfully discriminated against a profoundly deaf applicant by failing to arrange a sign interpreter for his 16 Dec 1997 interview; GBP2,500 awarded. Interview was adjourned and resumed 18 Dec 1997 with an interpreter present. A separate claim -- that he was not offered the job because of his disability -- failed at tribunal and on appeal (not an effective cause of the selection decision). Independently verified against the primary EAT transcript, 14 Sep 2026.', source:'Murphy v Sheffield Hallam University, EAT/6/99, [1999] UKEAT 0006_19_1101 (primary transcript, human-retrieved from BAILII 14 Sep 2026)', sourceUrl:'https://www.bailii.org/uk/cases/UKEAT/2000/6_99_1101.html', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'No documented UK standard or duty-holder split for accessibility of applicant-tracking systems / recruitment platforms', value:'Who carries the reasonable-adjustment duty when a candidate applies through a third-party recruitment agency or outsourced applicant-tracking system -- the agency, the platform provider, or the end employer, or all three concurrently -- is not settled by any published guidance or case found', source:'Project research pass, prompts 103-108 (Recruitment and hiring-stage access batch)', sourceUrl:'', lastVerified:'2026-09-14', status:'contested'}")

new_block = prefix + "\n" + ",\n".join(figs) + "\n  ]},"

content = content.replace(anchor, new_block, 1)
open("bsl_dossier.html", "w", encoding="utf-8").write(content)
print("done, new length:", len(content))
