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
figs.append("      {label:'Outsourcing an internal HR/IT/facilities desk does not switch off the employer Equality Act duty', value:'ss.20-21, 39, Sch. 8 remain the employer own duty; the contractor may separately owe a duty under s.31(5) where it provides a service only to the employer staff, treating those staff as a section of the public', source:'Equality Act 2010 ss.20-21, 39, 41(4), 31(5), Sch. 8; verified verbatim against legislation.gov.uk', sourceUrl:'https://www.legislation.gov.uk/ukpga/2010/15/section/31', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Access to Work funds the employee own communication support, not a contractor unpriced phone-only desk', value:'AtW can pay for a Deaf employee own video-relay minutes; it is not a grant that retrofits or varies a managed-service contract, and no official text describes it paying a contractor directly', source:'Project research pass, prompts 121-126 (Outsourced Services batch); AtW staff guide VRS definition', sourceUrl:'', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'Civil servants cannot apply to Access to Work -- but the underlying policy predates the 2025 wording change', value:'Departments have been responsible for their own civil servants workplace adjustments since 1 April 2022; the AtW staff-guide introduction was only edited on 13 November 2025 to state this plainly. Do not cite 13 Nov 2025 as the date eligibility changed.', source:'AtW staff guide update-history list; project research pass, prompt 124 (patched 14 Sep 2026 to add this distinction)', sourceUrl:'https://www.gov.uk/government/publications/access-to-work-staff-guide/access-to-work-staff-guide', lastVerified:'2026-09-14', status:'verified'}")
figs.append("      {label:'No published UK source reconciles BSL video-relay interpreting with whistleblowing anonymity', value:'A named interpreter on a VRS call becomes a witness to the disclosure; Safecall written-portal advice is one vendor recommendation, not a settled UK standard, and Protect own site shows a phone/web-form route rather than a confirmed BSL VRS product', source:'Project research pass, prompts 121-126 (Outsourced Services batch)', sourceUrl:'', lastVerified:'2026-09-14', status:'contested'}")

new_block = prefix + "\n" + ",\n".join(figs) + "\n  ]},"

content = content.replace(anchor, new_block, 1)
open("bsl_dossier.html", "w", encoding="utf-8").write(content)
print("done, new length:", len(content))
