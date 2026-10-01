# tailored-cv

A provider-neutral Agent Skill for producing truthful, vacancy-specific CVs, resumes, cover letters, screening answers, and explicitly authorized job applications.

The repository follows the open [Agent Skills](https://agentskills.io/specification) directory format used by compatible agent hosts. Runtime instructions avoid vendor-specific tool names, hardcoded executable paths, host-specific directories, and embedded candidate identities.

## Structure

```text
tailored-cv/
├── SKILL.md
├── assets/
│   └── cv-template.html
├── references/
│   ├── application.md
│   ├── candidate-profile.md
│   ├── rendering.md
│   └── writing.md
└── scripts/
    └── check_skill.py
```

`SKILL.md` is the entry point. Supporting files are loaded only for the relevant mode.

## Use with an agent

For an Agent Skills-compatible host, clone or copy this entire directory into a skills location recognized by that host, or upload the directory as a skill bundle. Installation paths and upload commands are host-specific; the skill content itself does not require changes.

For a host without automatic skill discovery, give the agent read access to this directory and instruct it to follow `SKILL.md`. File creation, PDF rendering, web access, and application submission still depend on the capabilities and permissions exposed by that host.

The skill intentionally contains no candidate profile. At runtime, the agent obtains personal and career data from the user's explicit statements, attached CV or resume, or a professional profile the user provides or authorizes. Missing identity or contact fields are requested before a final artifact is produced.

## Validate

Run the dependency-free portability check:

```bash
python3 scripts/check_skill.py
```

You can additionally run any validator that implements the Agent Skills specification.
