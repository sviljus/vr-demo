# Local production workflow

## Requirements

Python 3.10+, Node.js 20+, Georgia and Arial fonts (or the approved stylebook fallbacks). This repository is a document generator, not a deployed website. No API keys are required. Network access is needed only for initial dependency/browser installation; generated HTML embeds local image files.

```sh
cd /Users/viljauss/code/vr-demo
npm ci
python3 -m pip install -r requirements.txt
npx playwright install chromium
python3 scripts/validate.py data/reading-02.json
python3 scripts/build.py data/reading-02.json --out build/sample-02.html
node scripts/pdf.cjs build/sample-02.html build/sample-02.pdf
python3 scripts/build_docx.py data/reading-02.json --out build/sample-02.docx
```

The checked-in `reference/sample-02.pdf` is a known reference, not an output file to overwrite for each client. Compare the newly generated PDF against it. Reference page images are in `reference/pages/`. Generating files is not the same as inspecting them. Open/render every final PDF page before delivery. The blank `data/reading.template.json` intentionally fails production validation until all required content and crystal assets/credits are filled.

## A new Word upload

1. Follow `gen.md` and collect the user's review-consent answer. Do not infer consent from file contents.
2. Save the upload under ignored `incoming/` or another private working directory. Do not commit or publish it.
3. Extract and read all Word paragraphs and tables. Record source structure and factual commitments before rewriting.
4. Copy `data/reading.template.json` to ignored `build/client-reading.json` and fill its text and images from the edited source. Keep keys, role types, brand structure, and stylebook invariants.
5. Validate and build using that JSON. The sample's number, energy name, keywords, crystal associations, and products are examples, not universal source content.
6. Render the PDF. `scripts/pdf.cjs` measures actual PDF pages and adds a 6 mm progress bar. Page i of N has one pink segment spanning `(i−1)/N` to `i/N` of total page height. It is not cumulative.
7. Inspect every page. With consent and available tooling, obtain an independent review using `review/subagent-checklist.md`. Fix all blocking findings, regenerate, and recheck the final file.
8. Deliver private download links to BOTH the editable DOCX and PDF, optionally also HTML, plus a short Estonian change summary and honest review status. Never commit a personal result unless separately asked.

## Commands for arbitrary input/output files

```sh
python3 scripts/validate.py build/client-reading.json
python3 scripts/build.py build/client-reading.json --out build/client-reading.html
node scripts/pdf.cjs build/client-reading.html build/client-reading.pdf
python3 scripts/build_docx.py build/client-reading.json --out build/client-reading.docx
```

Use the same validated final JSON to build both outputs. `scripts/build_docx.py` populates an editable Word document using the template styles, real paragraphs, pictures, tables, hyperlinks and page-number fields. It requires `python-docx` from `requirements.txt`. This repository does not automatically import/edit the uploaded DOCX: the assistant must read it and perform the editorial mapping first. Word and HTML line wrapping can differ, so render and inspect both outputs. The PDF remains the fixed-layout design reference. Never substitute a renamed HTML file or a PDF of page images for a genuinely editable DOCX. Do not announce completion with one output missing unless the user explicitly accepts that limitation.

The HTML screen view shows progress by content group. The PDF uses actual physical page count. Manual browser printing does not apply PDF-lib postprocessing and must not be represented as the verified export path.

## Data and escaping

`data/reading.schema.json` documents the JSON shape. `scripts/validate.py` performs a dependency-free production check and verifies local asset paths. `scripts/build.py` runs validation before rendering, HTML-escapes source text, and embeds image bytes. It does not accept arbitrary HTML in text fields. Production links require HTTPS. Images must remain inside the repository and be covered by a source/license record.

`pages` contains content groups, not fixed-height containers. Each group begins on a new PDF page. Long content can add pages. Never shrink text below the stylebook to force exactly six pages. Crystal cards and galleries use `break-inside: avoid`; content taller than a physical page requires an editorial/layout decision.

## Dependency/runtime notes

`package-lock.json` locks the Node dependencies. Normal use resolves packages from local `node_modules`. The optional `VAIMURAAMAT_PLAYWRIGHT` and `VAIMURAAMAT_PDFLIB` environment variables select an existing package installation, as used during the initial artifact verification. They are not credentials. Do not commit machine-specific absolute paths.

For PDF images, a local Poppler installation can be used, for example:

```sh
pdftoppm -png -r 120 build/client-reading.pdf build/client-page
```

Only claim this visual check if it actually ran and every page was inspected. If rendering or delegated review is unavailable, explain the concrete limitation and agree on a fallback instead of pretending it happened.

## Git updates

```sh
git pull --ff-only
# Edit only approved public templates/docs/reference materials.
git status --short
git add gen.md stylebook.md templates scripts data assets docs review reference README.md AGENTS.md
git commit -m "Update Vaimuraamat document workflow"
git push
```

Before staging, check that no personal upload or output entered a tracked directory. Updating a canonical reference is a separate intentional design change: regenerate reference PDF and page PNGs together, document the reason, and rerun QA. Do not replace the canonical sample with a client's document.

## Required crystal-image research

For each crystal, open and visually inspect 3–4 candidate photographs, compare the recurring appearance against trusted mineralogical/museum/gemological identification, and verify the selected image's reuse rights. Use `review/crystal-image-review.template.md` to record source URLs, actual visual inspection, representative features, differences in lighting/form, rejection reasons, and the final author/license/credit. Majority resemblance is useful corroboration, not proof of identity. Do not count duplicate stock photos as independent confirmation. Existing sample photos do not establish that a new 3–4-photo search has occurred; record what was actually checked. If research is unavailable, state that and request an approved photo or explicit fallback.

## Final sign-off

Both builders share `scripts/closing.py`. They remove existing copies of the two brand sentences from ordinary text blocks and append one centered, separated final paragraph: “Iga number räägib oma loo. Iga kivi kannab oma energiat.” Do not add trailing content after this paragraph. Running footers are allowed.

## Offer data

`offer` blocks group `name`, `description`, `price`, optional `regular_price`, `cta`, HTTPS `url`, and optional `images` plus `caption`. Both generators render matching pale teal cards with large right-aligned prices. Product images belong inside the relevant card, not in a detached gallery. Sample CTA URLs are still homepage placeholders, not verified booking links. See `data/reading-02.json` for the exact shape.
