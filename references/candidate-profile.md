# Candidate profile and source policy

Use this policy before writing any candidate-specific content.

## Acceptable sources

Use candidate facts only from one or more of these sources:

1. details the user explicitly states in the current conversation;
2. a CV, resume, portfolio, profile export, or other document the user attaches or identifies as theirs;
3. a professional profile URL the user provides or explicitly authorizes the agent to use, such as LinkedIn;
4. relevant candidate facts already present in the visible conversation context.

Do not search for a person by name and assume a result is the user. Do not infer identity or contact details from account metadata, repository ownership, local paths, commit authorship, or unrelated files.

When a provided profile cannot be accessed or its identity is ambiguous, ask the user to attach an export, paste the relevant section, or confirm the source. Never bypass access controls.

## Personal data

Before creating a final candidate-specific artifact, establish:

- the display name;
- the contact methods the user wants included;
- location, timezone, or work authorization only when relevant;
- which professional-profile links may be included.

If these details are absent, ask one bundled question. If multiple approved sources conflict, ask which values are current. Never expose a home address, government identifier, date of birth, marital status, photograph, or other sensitive detail unless the user explicitly requests it and it is appropriate for the destination.

Use data minimization: include only details useful for the application. Do not persist candidate data into the skill itself.

## Claim ledger

Maintain a lightweight internal ledger while drafting:

| Claim | Source | Employer or context | Role and dates | Status |
| --- | --- | --- | --- | --- |
| Candidate fact or metric | Exact source location | Relevant organization | Known period or `unassigned` | verified / needs clarification |

The ledger need not be shown unless useful, but it must govern the output.

Rules:

- Preserve exact dates and values from the source.
- Do not strengthen approximate metrics into exact ones.
- Do not merge separate achievements into a causal story unless the source supports it.
- Do not assign an `unassigned` achievement to a role. Keep it at employer level or ask for the period.
- Treat a technology named only in the vacancy as unsupported until a candidate source confirms it.
- Treat explicit user corrections as authoritative for the current task; mention unresolved contradictions before finalizing.

## Gap questions

Ask only about gaps that affect fit, accuracy, or submission. Group related questions, preferably into one round and at most two rounds unless the user invites a deeper interview.

Good subjects include:

- identity or contact fields required for the artifact;
- must-have technologies or domains absent from the sources;
- ambiguous role attribution or dates;
- salary, relocation, visa, work authorization, notice period, or travel;
- a metric the user may know and that would materially strengthen a verified achievement.

If the user does not answer, continue with supported facts and identify the omission. Never fill the gap with a plausible assumption.
