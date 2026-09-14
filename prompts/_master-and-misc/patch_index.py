content = open("SuperGrok_Research_Prompt_Pack.md", encoding="utf-8").read()

old_header = "**⚠️ NEXT PROMPT NUMBER TO USE: 170.** The highest prompt number issued anywhere in this project so far is **169** (see the index below). Before adding a new section to this file, check this line, confirm it against the index table, then start your new prompts at the next free number and update this line and the index in the same edit. Never start a new batch back at 1 -- see \"Numbering discipline\" below for why this matters."
new_header = "**⚠️ NEXT PROMPT NUMBER TO USE: 171.** The highest prompt number issued anywhere in this project so far is **170** (see the index below). Before adding a new section to this file, check this line, confirm it against the index table, then start your new prompts at the next free number and update this line and the index in the same edit. Never start a new batch back at 1 -- see \"Numbering discipline\" below for why this matters."
assert content.count(old_header) == 1, "header anchor found %d times" % content.count(old_header)
content = content.replace(old_header, new_header, 1)

anchor_line_start = "| 168–169 |"
idx = content.index(anchor_line_start)
line_end = content.index("\n", idx)
existing_line = content[idx:line_end]
assert existing_line.endswith("170 stays next-free. |")

new_row = "| 170 | Single-prompt patch to 103-108 (Recruitment and hiring-stage access): locate and quote the primary EAT transcript for *Murphy v Sheffield Hallam University* (EAT/6/99, [2000] EAT 6/99/1101, 11 Jan 2000, HHJ Peter Clark) to confirm or correct three details previously cited only from a secondary case-note site (swarb.co.uk) -- the GBP2,500 award, the 16/18 December 1997 dates, and the \"amateur signer\" characterisation. Verification-only; does not reopen recruitment-stage legal analysis (already covered by 103-108). Explicit instruction to report an access failure honestly rather than restate the secondary source as if newly verified. | Prompt text: `claude/grok-prompt-170-murphy-sheffield-hallam.md` (project) / `prompts/Recruitment-Hiring/Recruitment-prompt-170-murphy-sheffield-hallam-transcript-verification.md` (this folder) | Issued 14 September 2026, not yet run. Background: automated WebSearch/WebFetch located the case citation (EAT/6/99) but a direct BAILII fetch was blocked by BAILII's own bot-protection layer (Anubis); no mirror or alternative primary source surfaced. Standing restriction pending this prompt's result: do not quote the GBP2,500 figure or the December 1997 dates publicly. |"

content = content[:idx] + existing_line + "\n" + new_row + content[line_end:]

open("SuperGrok_Research_Prompt_Pack.md", "w", encoding="utf-8").write(content)
print("done, new length:", len(content))
