# Independent final review brief

Use only after the user has explicitly consented to a real subagent reviewing this document. If you are the main assistant and no subagent capability exists, do not impersonate an independent reviewer. Follow the fallback in `gen.md`.

## Inputs required

Obtain the latest source Word document or source-to-edited mapping, latest edited JSON/text, final PDF and editable DOCX generated from the same finalized content, rendered page PNGs for both, `stylebook.md`, `reference/sample-02.pdf`, `reference/sample-02.docx` and the reference page PNGs. Also obtain the per-crystal 3–4-candidate photograph audit, `assets/manifest.json`, image credits, any confirmed price changes, and explicitly approved design deviations. If an input is missing, identify it and state what cannot be verified.

Record the exact artifact version or file hash. Review the final build, not an earlier draft. Do not rewrite the whole reading unsolicited, and do not approve merely because the main assistant asks you to confirm it is good.

## Required checks

### 1. Source fidelity and Estonian

- Read the entire edited text against the source. Important ideas, examples and practical steps remain intact.
- Correct spelling, inflection, punctuation, sentence construction, natural word order and `sina` voice.
- Point A remains the correct specific position; energy number, name, keywords and body references agree.
- No example's number 2 content has leaked into another energy without support.
- Stylistic edits are distinguished from substantive additions/removals.
- Numerology and crystal associations remain symbolic; no deterministic diagnosis, childhood assertion, supernatural ability, future certainty or healing promise has been introduced.
- Offers and prices match the confirmed source; no invented scarcity, discount or testimonial.

### 2. Stylebook and assets

- Correct website logo, proportional shape, palette, hierarchy and readable type sizes.
- Calm masthead, clear energy identity, examples, exercise, crystal cards and optional offers follow the component rules.
- Crystal images are real, correctly identified photos, not the rejected geometric drawings or fabricated specimen photos.
- For EACH crystal, the audit contains 3–4 candidate photos with source/image URLs, truthful actual visual-inspection status, identity checked against a reliable mineral/museum source, form/lighting/appearance notes, representative-majority comparison, selection/rejection reasons, rights and attribution. Majority resemblance alone must not establish identity. Check rough versus tumbled/cut differences and avoid rainbow moonstone/labradorite mislabeling.
- Do not assume committed sample photos already passed this newly required audit; require retrospective evidence if absent. Missing image access is a limitation, not a passed check.
- Credit text, original-source links and license links are present and agree with the manifest.
- Bracelet photographs are examples and have a caption stating the custom composition may differ.
- Any intentional deviation is user-approved and documented rather than concealed.

### 3. Every-page layout comparison

Verify that BOTH an editable Word `.docx` and PDF exist and contain the same final edited content. Inspect rendered pages of both; Word pagination may differ, but typography, components and readability must follow the same system. A missing format requires an explicit user waiver, not a silent substitution.

Open every final page image and compare with the corresponding design system in the reference. Do not rely only on extracted text or page 1.

Check margins, alignment, line spacing, heading hierarchy, paragraph rhythm and component widths. Look for clipping, overlap, missing glyphs, stretched photos, text touching borders, orphan headings, split questions/quotes/cards and nearly empty accidental overflow pages. Confirm footer positions, clickable domain, sequential page numbers and working action links.

The page count can differ from the six-page example. A matching layout preserves the design system and readable content flow, not identical paragraph line breaks. Do not demand text deletion to force the reference's page count.

For N actual PDF pages, confirm the full-height 6 mm right-edge track and a pink moving segment of height H/N on each page. Segment i starts `(i−1)H/N` below the top. First segment reaches the top and last reaches the bottom. It is not cumulative and must use actual PDF pages, including overflow pages.

## Report format and decision

Use the fields in `review/report.template.md` when available. Return:

1. reviewed artifact/version and available evidence;
2. outcome: `PASS`, `FIX_REQUIRED` or `BLOCKED`;
3. separate outcomes for source/language, style/assets and rendered layout;
4. findings with severity, exact page/section, observed evidence, violated rule and concrete correction;
5. unverified items and explicit limitations.

Use `BLOCKED` if either required Word/PDF artifact, their rendered visual evidence, or the mandatory crystal candidate-image audit cannot be inspected and no specific user waiver exists, rather than asserting layout conformity. Use `FIX_REQUIRED` for material language, source, rights, price, clipping or progress errors. Minor editorial suggestions should be identified as suggestions rather than blocking defects.

Do not claim certainty about facts absent from the source. Do not send documents to third-party services or commit them to the public repository. The main assistant must apply confirmed corrections, regenerate affected artifacts and recheck the revised final version before announcing completion.
