# Canonical visual reference

`sample-02.pdf` is the canonical HTML-generated number 2 reading, six physical A4 pages. `pages/page-01.png` through `page-06.png` are renders of this exact PDF at 100 dpi. `manifest.json` records their hashes and the baseline page count. The source is `data/reading-02.json`; the design specification is `stylebook.md`.

Use this sample to compare design and components, not as the factual source for another energy. Different content may require more or fewer pages. Preserve the dynamic right-edge segment formula using the actual output page count.

This baseline includes real crystal photographs with source/license credits, the website logo, two bracelet product examples, navy/teal/pink brand furniture and the moving progress segment. The earlier geometric illustrations are excluded. The manual DOCX template is a separate convenience and is not the canonical renderer.

When a design change is explicitly approved, regenerate the PDF and page images together, update the manifest, and inspect every page. Ordinary client documents must go to ignored `build/`, not this folder.
