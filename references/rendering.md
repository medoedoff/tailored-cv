# Rendering and artifact verification

Use these instructions only when the user requests a formatted file or PDF.

## Portable rendering

Start from [assets/cv-template.html](../assets/cv-template.html) when an HTML-to-PDF route is suitable. Replace every placeholder with verified content and remove unused sections.

Use the document or rendering capability available in the current environment. Do not assume:

- a specific browser, binary, package, operating system, home directory, or temporary directory;
- permission to install dependencies;
- a named file-transfer tool;
- that a command succeeded without inspecting its result.

Work in a permitted workspace or temporary directory. Save the final artifact where the user or host environment expects deliverables. Sanitize generated filenames to a portable form such as `Candidate_Role_Company.pdf`; remove path separators and reserved characters.

If a required renderer is unavailable, preserve the completed HTML or document source and explain what capability is missing. Ask before installing software or using an external conversion service.

## Layout priorities

Use this order when content does not fit:

1. remove repetition and unsupported or low-relevance content;
2. tighten long bullets and the summary;
3. reduce optional spacing;
4. use an additional page if the requested format permits it;
5. reduce typography only while it remains comfortably readable.

For an A4 CV, do not go below 9 pt body text unless the user explicitly approves a smaller size. Do not hide overflow, clip text, or shrink content solely to satisfy a page-count target.

## Verification

Perform every check supported by the environment:

- open the artifact successfully;
- confirm the requested page size and acceptable page count;
- render pages to images and inspect alignment, clipping, wrapping, spacing, and blank areas;
- extract text to confirm the PDF is searchable and contains the expected sections;
- verify contact and profile links;
- check that no placeholder remains;
- confirm the final filename and file type;
- compare visible content with the verified candidate profile.

Report which checks were completed. Never state that visual or PDF verification passed when it was not performed.
