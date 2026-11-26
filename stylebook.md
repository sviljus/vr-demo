# Vaimuraamat stylebook

Version 1.0 · 26 November 2026. This English specification governs the Estonian reading series. Read it together with `gen.md`. The canonical rendered example is `reference/sample-02.pdf`; the HTML/CSS implementation is `templates/reading.html`. A current explicit user design change overrides this specification and should be recorded as a deviation.

## Design purpose

The reading should feel like a carefully edited small publication, personal and useful without a purchase. It is not a product catalogue, horoscope making certain claims, or a loud esoteric campaign. The brand connection comes from the website logo, deep navy, teal and restrained pink. White reading surfaces, generous whitespace and controlled typography take precedence over decoration.

Do not reproduce the discarded arbitrary geometric crystal drawings. Use real, correctly identified photographs and proper attribution. Do not introduce neon colors, gradients, glow effects, ornamental borders or a cosmic image behind body text.

## Authority and invariants

Mandatory visual invariants are logo proportions and identity, type hierarchy, body readability, brand palette, semantic section order, repeated component structure, unobtrusive offers, a consistent footer, and the page-count-dependent progress bar. The sample's six pages are an example, not a maximum or a universal page-count target.

Variable content includes the energy number, name, three keywords, introduction, body, examples, lesson, exercise, crystals and verified offers. Paragraph line breaks, chapter continuation and final page count may change with length. Preserve useful content rather than compressing it into the sample's exact breaks. Report an approved redesign honestly instead of describing it as identical to the original reference.

## Color tokens

| Token | HEX | Use |
|---|---|---|
| Main text | `#192B43` | Body, headings, links |
| Deep navy | `#111629` | First-page masthead |
| Brand teal | `#57A7B3` | Website logo, fine footer rule |
| Brand pink | `#EC6A87` | Active segment of the side-progress bar |
| Pale teal | `#EFF6F6` | Quiet cards, callouts and progress track |
| Gold | `#B18A49` | Central energy number; sparing accent only |
| Secondary text | `#647080` | Labels, supporting text and footer |
| Ivory | `#FAF8F3` | Crystal-card surface where used |
| White | `#FFFFFF` | Principal reading surface |

Do not use gold or pale teal for small essential body text. Maintain sufficient contrast. Do not reinterpret the logo colors or stretch the logo to fill a space.

## Page geometry and typography

The canonical HTML print route uses A4, portrait, 210 × 297 mm. Print margins are top 20.5 mm, left/right 20.5 mm and bottom 17 mm. The masthead is 28 mm high and sits within the printable content area; it is not a clipped negative-margin bleed. The 6 mm progress bar sits at the physical right edge and is drawn after pagination.

| Element | Typeface | Size and treatment |
|---|---|---|
| Energy number | Georgia | 68 pt, gold, centered, line-height approximately 0.95 |
| Main title | Georgia | 27 pt, navy, centered |
| Energy name | Georgia | 14 pt, bold, centered |
| Keywords | Arial | 11 pt, secondary color, centered |
| Chapter heading | Georgia | 17 pt, bold, navy |
| Subheading/card name | Georgia | 14 pt, bold, navy |
| Main body | Arial | 10.5 pt, line-height 1.4 |
| Highlighted thought | Georgia | 13 pt, italic, line-height 1.3 |
| Card text | Arial | 10 pt, line-height 1.3 |
| Small label/tagline | Arial | 8.5 pt |
| Footer/running header | Arial | 8 pt |
| Photo credit | Arial | 7.5 pt, readable, linked |

Use Georgia/Arial as the implemented reference fonts. If unavailable, use a comparable serif/sans-serif pair, disclose the substitution and inspect all reflow. Do not distribute proprietary font files without rights. Body paragraphs are left-aligned, with approximately 7 pt after each. Avoid full justification, stretched tracking and forced line breaks merely to imitate one reference line.

## Cover and running furniture

First-page order: navy masthead with centered website logo; the tagline “Isiklik hetk iseenda avastamiseks”; large number; “Sinu Punkt A energia”; number and energy name; three keywords separated by middle dots; opening reflection; introduction and beginning of the reading. Do not put “tasuta” prominently in the masthead. Preserve “Punkt A”.

The central number is the visual focus. Do not add decorative rings, glow or random mystic symbols. Keep the text outside the dark logo masthead on a light surface.

Running headers are small and quiet: brand at the left, Point A context at the right. The footer has a fine teal rule, “Vaimuraamat” left, a clickable `vaimuraamat.ee` centered and the automatic page number right. It must not collide with the body, wrap awkwardly or repeat the current browser URL and print date.

The manual DOCX template uses Word styles and may have different pagination and masthead geometry. It is not the canonical print rendering. Ordinary edits must not promise that Word automatically recalculates the pink segment after arbitrary page-count changes.

## Side-progress indicator

Let N be the number of physical pages in the completed PDF, H the physical page height and i the one-based page number. The right-edge track is 6 mm wide and pale teal for the full height. Pink occupies the vertical interval measured from the top:

`start = (i − 1) × H / N`

`end = i × H / N`

Thus three pages show one moving third, five pages one moving fifth, six pages one moving sixth. This is not a small fixed dot and not a cumulative progress fill. Page 1 starts at the top; the last segment reaches the bottom. Compute N after Chromium pagination; never use JSON content-group count as the final PDF page count. The HTML screen view may indicate content-group position because it has no physical A4 pagination. The PDF exporter is authoritative.

## Section and component system

Maintain the semantic progression: introduction → energy essence → balanced energy → difficult patterns → life lesson → exercise → crystals → continuation and optional offers. Numbered headings are optional. Do not leave a heading at the foot of a page without subsequent text.

**Energy identity:** number, energy name and exactly three keywords must agree everywhere. These are data, not a rasterized image of text.

**Highlighted thought:** one short substantive idea in Georgia on a pale surface. Keep it together. Avoid repeated ornamental slogans.

**Everyday example:** mark with “Näide igapäevaelust”, followed by a concrete source-faithful paragraph. Keep a normal-length example together when possible. Do not invent experiences or testimonial claims.

**Exercise:** “Hetk iseendale” opens a practical task. Separate questions visually with quiet card treatment. Keep each question intact. Include a usable action or reflection without requiring a purchase, ritual or special object.

**Crystal cards:** two equal columns in the reference, each with real photo, name, symbolic meaning, energy connection, personal reminder and credits. Photo box: 56 × 32 mm, `object-fit: contain`, original aspect ratio preserved. Do not crop away the stone, mislabel a specimen or imply a photo is a specific shop product when it is not. Keep cards together where feasible. A card taller than an entire page requires an editorial/layout decision; do not fix it by shrinking to unreadable type.

The sample photograph sources are Ozguy89's public-domain uncut rose quartz and Ra'ike's moonstone image derived from Simon Eugster, used under CC BY 2.5. Preserve the exact credits and license links from the data and asset manifest. Asset appearance is illustrative and does not establish any claimed metaphysical effect.

**Bracelet gallery:** two brand example photographs, approximately 56 mm high, aspect ratio retained. Include the caption explaining that the personal selection of stones and pendant can differ. A gallery is not evidence that the pictured bracelet is the prescribed number 2 product.

**Offers:** under “Kui soovid edasi avastada”, show each service's name, one or two calm descriptive sentences, confirmed price and a modest HTTPS link. No false urgency, invented discount, oversized banner or testimonial. Let the reading feel complete before the sales section and let the final line leave the reader free to stop.

## Estonian editorial standard

Use natural, warm, concise Estonian in `sina` form. Preserve the author's substance and useful examples. Fix spelling, grammar and awkward repetition; distinguish these from meaning changes in the audit. Do not replace clear original language with inflated prose.

Keep “Punkt A”, “energia”, the confirmed energy name, “tasakaalus energia”, “energia keerulisemad küljed”, “eluõppetund” and “kristallide sümboolne tähendus” consistent. Explain “pluss” and “miinus” if retained. Prefer “number 2 energia” or “sinu energia” to repetitive “2. energia”.

Frame numerology and crystal associations as symbolic interpretation. Do not infer childhood, abilities, diagnosis, relationships or future with certainty from a birth date. Do not promise healing or life-event effects from stones. The reader may reject any interpretation. Use practical invitations instead of assertions that the reading has revealed a proven part of them.

## Release quality

Validate the data, render the actual output and inspect every page. Check all Estonian characters, headings, questions, photos, credits, links, prices, footer and progress positions. Match the reference's system while allowing content-driven pagination. Remove duplicate links, clipping, collisions, split cards and accidental nearly empty overflow pages.

Before completion, apply the independent-review consent workflow in `gen.md`. A technical build pass is not linguistic review; extracted text is not visual review; self-review is not an independent subagent. Record remaining limitations and the version actually checked. Never call an unverified draft complete.
