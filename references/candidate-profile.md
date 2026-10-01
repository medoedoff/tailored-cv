# Candidate profile and source policy

Use this policy before writing any candidate-specific content.

## Candidate source gate

Before drafting any CV, resume, cover letter, or screening answer, verify that the current conversation contains at least one of these sources:

1. an attached CV or resume in PDF, DOCX, TXT, or MD format that the user identifies as theirs;
2. a LinkedIn profile URL supplied by the user, or a LinkedIn PDF export;
3. a pasted work history that gives the employer, job title, dates, and achievements for every role.

The source must be readable and attributable to the user. A LinkedIn URL does not pass the gate when its contents cannot be retrieved because of a login wall, blocked fetch, or similar access restriction. Do not reconstruct it from search results or snippets; ask for a LinkedIn PDF export or the CV file instead. Do not search for a person by name and assume a result is the user.

If no qualifying source is present, ask once, in the user's language, for a current CV or a LinkedIn profile link or export. Explain in one sentence that it is needed to place experience under the correct roles. Until the user provides one:

- do not generate, render, or save a CV, resume, cover letter, or screening answers;
- do not build a candidate profile from facts scattered across the conversation, earlier sessions, memory, or the skill itself;
- for vacancy searches, return only the vacancy list in the format defined by `Presenting search results` in [job-sources.md](job-sources.md), omit candidate-fit claims, and end with one line asking for the CV or LinkedIn source so tailored CVs can be created next.

Do not repeat the request if it was already made in the current conversation; state only that the gate remains unmet if necessary.

## Master profile and supplementary facts

Once the gate passes, use the qualifying source as the master profile. Preserve its employers, roles, date structure, and role attribution. A role-attributed CV or resume, a readable LinkedIn profile or export, or a complete pasted work history may serve as the master profile.

After establishing the master profile, supplement it only with details the user explicitly states in the current conversation, including corrections and answers to gap questions. Do not use earlier sessions, memory, account metadata, repository ownership, local paths, commit authorship, unrelated files, or candidate data embedded in the skill.

If multiple approved sources conflict, ask which one is current. Never bypass access controls. Do not persist any candidate data into the skill.

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
- Do not assign an `unassigned` achievement to a role. Ask which role it belongs to; use an employer-level block only when the master source itself does not attribute it and the user cannot resolve the attribution.
- Treat a technology named only in the vacancy as unsupported until the master profile or the user's gap-question answer confirms it.
- Treat explicit user corrections as authoritative for the current task; mention unresolved contradictions before finalizing.

## Gap questions

Ask only about gaps that affect fit, accuracy, or submission. Group related questions, preferably into one round and at most two rounds unless the user invites a deeper interview.

Good subjects include:

- identity or contact fields required for the artifact;
- must-have technologies or domains absent from the sources;
- ambiguous role attribution or dates;
- salary, relocation, visa, work authorization, notice period, or travel;
- a metric the user may know and that would materially strengthen a verified achievement.

Before drafting, compare every technology, tool, and platform named in the vacancy's must-have and nice-to-have requirements with the master profile. Put every missing item into one consolidated question, with each technology as its own yes/no option phrased `Have you worked with X?`. Never phrase the question as `Should I add X?`.

Ask this technology question once and wait for the user's reply before drafting. Treat every `no`, declined item, and item left unanswered in the reply as unconfirmed. A confirmation supports only the technology and any context the user explicitly supplies; it does not support invented metrics, scale, duration, or role history.

If the user does not answer, continue with supported facts and identify the omission. Never fill the gap with a plausible assumption.
