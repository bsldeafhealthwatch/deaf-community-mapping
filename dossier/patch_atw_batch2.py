import re

path = "bsl_dossier.html"
content = open(path, encoding="utf-8").read()

start = content.index("id:'access-to-work'")
rest = content[start:]
end_marker = rest.index("\n  { id:")
block = rest[:end_marker]
anchor = block[-350:]
assert content.count(anchor) == 1, "anchor found %d times" % content.count(anchor)

# Strip the trailing closing bracket so we can append new figures before it
close_tail = "\n  ]},"
assert anchor.endswith(close_tail)
prefix = anchor[:-len(close_tail)] + ","

figs = []
figs.append("      {label:'No statutory clock for employer to fulfil an agreed reasonable adjustment', value:'ACAS: reasonableness on the facts, no fixed days figure. Work and Pensions Committee has asked for a 2-week written response (not a fulfilment deadline) as a recommendation, not law.', source:'ACAS, Reasonable adjustments at work (updated 30 Jan 2025); WPC HC 1227, 21 May 2026', sourceUrl:'https://www.acas.org.uk/reasonable-adjustments-at-work', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Equality Act reasonable-adjustment duty covers agency and contract workers, not just employees', value:'s.41(4) and Sch. 8 can put the duty on both the hirer and the agency/principal', source:'Equality Act 2010 ss.20, 21, 39, 41, Sch. 8', sourceUrl:'https://www.legislation.gov.uk/ukpga/2010/15/section/41', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Illustrative tribunal case: employer/agency delay on assistive-tech kit', value:'Khan v Reed Talent Solutions Ltd (ET 1801643/2024) upheld s.20/21/41(4) breach on 7 of 9 items; kit-delivery evidence in the judgment sits Aug-Oct 2023 (chair estimate 9 Oct 2023), across a multi-entity employment chain (PayStream, then Reed PAYE, then SWES) before direct council employment began 3 Nov 2023. Not a Deaf/BSL case -- cited only as an illustration of a documented internal-ticket delay reaching tribunal.', source:'ET 1801643/2024 judgment (GOV.UK employment tribunal decisions register)', sourceUrl:'https://www.gov.uk/employment-tribunal-decisions', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'No documented in-house-staff-served-first ticketing rule found', value:'No published contract, FOI response, CIPD/REC report or judgment locating this practice as policy', source:'Project research pass, prompts 97-102 (HR/IT SLA batch)', sourceUrl:'', lastVerified:'2026-09-14', status:'contested'}")
figs.append("      {label:'Workplace Adjustment Passport is a voluntary, employer-held record, not an automatic legal guarantee for the next employer/contract', value:'Royal Mail own passport scheme expressly excludes agency workers, contractors and the self-employed', source:'Civil Service, NHS Employers and TUC/GMB model passport guidance; Royal Mail scheme terms', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'NRCPD and RBSLI are voluntary registers, not statutory regulators', value:'No UK statute makes unregistered BSL interpreting a criminal offence; statutory regulation is NRCPD own stated long term aim with no published timescale', source:'NRCPD, Statutory regulation page (fetched live 13 Sep 2026)', sourceUrl:'https://www.nrcpd.org.uk/statutory-regulation', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Registered Interpreters for Deafblind People (RIDB), national total', value:'19 live nationally (13 Sep 2026 spot-check), against a GOV.UK 23 June 2026 grant target of 68 from a baseline of 8; East Midlands, South West and Yorkshire and The Humber all show zero registrants', source:'NRCPD registration-figures page; GOV.UK RIDB grant announcement', sourceUrl:'https://www.nrcpd.org.uk/registration-figures', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Sign Language Interpreter register total', value:'1,664 (spot-checked live 13 Sep 2026); figure includes dual registrations across categories per NRCPD own caveat, so is not a unique-person headcount', source:'NRCPD registration-figures page', sourceUrl:'https://www.nrcpd.org.uk/registration-figures', lastVerified:'2026-09-14', status:'verified'}")

new_block = prefix + "\n" + ",\n".join(figs) + "\n  ]},"

content = content.replace(anchor, new_block, 1)
open(path, "w", encoding="utf-8").write(content)
print("done, new length:", len(content))
