---
name: ArcaneByte
description: A small maker's shop in the shape buyers already know, built from a black bar, a navy hero, and 4-up rows of hand-built Lisa hardware.
colors:
  page-white: "#ffffff"
  ink: "#121212"
  ink-soft: "#595959"
  line: "#e5e5e5"
  tile-gray: "#f3f3f3"
  tile-gray-press: "#ebebeb"
  bar-black: "#000000"
  bar-divider: "#2a2a2a"
  photo-backing: "#111111"
  navy: "#1f2a44"
  action-blue: "#2b5fd9"
  action-blue-deep: "#244fb5"
typography:
  display:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "clamp(2rem, 4vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "clamp(1.75rem, 3vw, 2.25rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  subtitle:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  lede:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "normal"
  small:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
  fine:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  base: "4px"
  inner: "3px"
spacing:
  gutter: "clamp(1rem, 4vw, 2.5rem)"
  band: "clamp(2.5rem, 6vw, 4.5rem)"
  group: "3.5rem"
  grid-gap: "2.25rem 1.25rem"
  stack: "1rem"
  page: "1180px"
  narrow: "760px"
  measure: "68ch"
  bar: "76px"
components:
  button-primary:
    backgroundColor: "{colors.action-blue}"
    textColor: "{colors.page-white}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "0.75rem 1.875rem"
  button-primary-hover:
    backgroundColor: "{colors.action-blue-deep}"
    textColor: "{colors.page-white}"
  button-secondary:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "0.75rem 1.875rem"
  button-secondary-hover:
    backgroundColor: "{colors.tile-gray-press}"
    textColor: "{colors.ink}"
  button-white:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "0.75rem 1.875rem"
  button-white-hover:
    backgroundColor: "{colors.tile-gray-press}"
    textColor: "{colors.ink}"
  header-bar:
    backgroundColor: "{colors.bar-black}"
    textColor: "{colors.page-white}"
    typography: "{typography.body}"
    height: "{spacing.bar}"
  hero-panel:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.page-white}"
    rounded: "{rounded.base}"
    padding: "3.5rem 3.25rem"
  product-tile-photo:
    backgroundColor: "{colors.photo-backing}"
    rounded: "{rounded.base}"
  product-tile-label:
    backgroundColor: "{colors.tile-gray}"
    rounded: "{rounded.base}"
    padding: "10%"
  store-row:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.base}"
    padding: "1.1rem 1.25rem"
  store-row-hover:
    backgroundColor: "{colors.tile-gray}"
    textColor: "{colors.ink}"
  notice:
    backgroundColor: "{colors.tile-gray}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.body}"
    rounded: "{rounded.base}"
    padding: "1rem 1.15rem"
  footer:
    backgroundColor: "{colors.tile-gray}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "3rem 0 1.75rem"
---

# Design System: ArcaneByte

## Overview

**Creative North Star: "The Parts Counter"**

ArcaneByte looks like a small hardware maker's shop and nothing else: a black bar with the floppy mark and the wordmark, a navy panel beside the lead photo, and the goods laid out in 4-up rows on a white page. The owner's reference is shop.bigmessowires.com, and the refusal is any costume. There is no theme, no period chrome, no section the landing page does not need. The landing page is the hero and the product groups, by the owner's decision, and everything else (About, ordering notes, policies) waits in the footer or on its own page.

The page is flat and quiet. Corners are 4px everywhere, photos sit in a 1px hairline frame on near-black backing, printed labels for unbuilt products sit whole on a light gray tile, and nothing casts a shadow at any state. The only color the site adds is the black bar, the navy hero panel, and one blue for a primary button; the boards in the photographs supply everything else. Inter is the single face, 700 for headings, 500 for buttons and tile names, 400 for text, and nothing is set in caps or tracked out.

Density is a shop's, not a magazine's: body text runs at 15px, tile names at 14px, and the product page puts the title, fit line, PayPal's own widget, and three perks in one column beside the photo. PayPal prints its own title, price, and description inside the buy column, so the site adds only what PayPal does not say, and no price appears anywhere else on the site.

**Key Characteristics:**
- Black header bar, navy hero panel, white page, light gray footer; 4px corners throughout
- One blue (`action-blue`) for the primary button and link hover; the bar and the navy are the only other color
- Inter is the only face; 700 headings at −0.02em, 500 labels, 400 text; no caps, no tracking, no eyebrows
- Flat at every state: no shadow, no lift, no blur; hover is a fill change or an underline
- Photos cropped 4:3 in a hairline frame on near-black; printed labels shown whole on a gray tile
- The landing page is the hero and the product groups, grouped by what the product is for

## Colors

A white page with a black bar and a navy panel, one blue for the primary action, and grays for text and tiles; the saturated color on the site is the product photography.

### Primary
- **Action Blue** (`action-blue`): the fill and border of the primary button ("Email about …", "Email to order" in the buy column) and the hover color of underlined links in prose, the guide link, and the "Also sold on" store links. It is not used for links at rest.
- **Action Blue Deep** (`action-blue-deep`): the primary button's hover fill only.

### Secondary
- **Navy** (`navy`): the hero panel behind the headline, and the page's text-selection color (inside the hero, selection inverts to white on navy).
- **Bar Black** (`bar-black`): the header bar on every page and the mobile nav sheet. Text on it is pure white.
- **Bar Divider** (`bar-divider`): the hairlines inside the mobile nav sheet, between links and under the bar.

### Neutral
- **Page White** (`page-white`): the page, the secondary button, the hero's white button, store rows, and the "Add to Cart" column.
- **Ink** (`ink`): headings, body text, tile names, the secondary button's border, the FAQ chevron, perk icons, and table header rules.
- **Ink Soft** (`ink-soft`): ledes, tile fit lines, group notes, captions, notices, FAQ answers, the "Fits" label, the "In development" dot, the "Also sold on" line, the footer base, and blockquotes. Passes 4.5:1 on white and on Tile Gray.
- **Line** (`line`): the 1px frame on every photo and thumbnail, the buy column's rule above PayPal's widget and above the perks, FAQ rows, table rows, `hr`, store row borders, and the footer base rule.
- **Tile Gray** (`tile-gray`): the label tile behind an unbuilt product's printed label (in the grid and on its product page), the footer, notices, inline code and code blocks, the "Photo to come" plate, and the store row's hover fill.
- **Tile Gray Press** (`tile-gray-press`): the hover fill of the secondary and white buttons.
- **Photo Backing** (`photo-backing`): the near-black behind every product photo (hero, tile, product plate, thumbnails, gallery), so a photo that loads late or has transparent corners reads as a dark plate rather than a hole. This is a literal in the stylesheet, not a custom property.

### Named Rules
**The One Blue Rule.** Blue is the primary button's fill and a link's hover color, nowhere else. Links at rest are ink, underlined. Tiles, borders, icons, the state dot, and the FAQ chevron are ink or gray. PayPal's yellow "Add to Cart" is PayPal's widget, outside the system; nothing on the site echoes it.

**The Three Colors Rule.** The site adds exactly three colors to a white page: the black bar, the navy hero panel, and the blue button. Every other surface is white or a gray. A new surface is white, or Tile Gray if it is a tile, a notice, or the footer.

**The Photo Carries the Color Rule.** The red, white, black, and green boards are the color on the page. Photos are shown in true color, never tinted, faded, or duotoned, and the backing behind them is near-black so the boards read as the photographed objects.

## Typography

**Display Font:** Inter (self-hosted variable, weight 100–900, latin and latin-ext subsets; `system-ui` fallback)
**Body Font:** Inter
**Label/Mono Font:** none for labels. `code`, `kbd`, and `pre` use `ui-monospace, "SF Mono", Menlo, Consolas, monospace` at 0.92em, for actual code only.

**Character:** One grotesque at normal width. Headings are bold, tightened to −0.02em, balanced, and set at 1.15; running text is 15px at 1.6. Numbers are tabular across the site so model numbers and dimensions line up. Nothing is uppercase, nothing is letter-spaced, and no heading has a kicker above it.

### Hierarchy
- **Display** (700, `clamp(2rem, 4vw, 2.5rem)`, 1.15, −0.02em): the page `h1` on FAQ, Where to buy, and the catalog section pages. The hero sets its `h1` at a fixed 2.5rem (2rem below 900px) in white, capped at 14ch; the product title is `clamp(1.75rem, 3.2vw, 2.25rem)`.
- **Headline** (700, `clamp(1.75rem, 3vw, 2.25rem)`, 1.15, −0.02em): product group headings ("For the Apple Lisa", "For anything with an RS232 serial port").
- **Title** (700, 1.375rem): "Product details", "You may also like", and `h2` inside prose.
- **Subtitle** (700, 1.125rem): bare `h3`. Inside prose, `h3` ("Features", "Planned features") steps down to 1.0625rem; `h4` and footer column headings are 0.9375rem at 700.
- **Lede** (400, 1.0625rem, Ink Soft): the line under a page `h1`, max 60ch. The product lede is 1rem at 48ch; the hero's is body size in white at 92%, 42ch.
- **Body** (400, 0.9375rem, 1.6): running text at a 68ch measure, nav links, the FAQ answer, and notices.
- **Label** (500, 0.9375rem, 1.2, sentence case): buttons. Tile names are 500 at 0.875rem/1.4; the "In development" state line is 500 at 0.875rem; the FAQ question is 600 at 1rem.
- **Small** (400, 0.875rem): tile fit lines (0.8125rem), the "Fits" row, perks, the store links line, captions, "Photo to come", and the store row's second line.
- **Fine** (400, 0.8125rem, Ink Soft, centered): the footer base line.

### Named Rules
**The Sentence Case Rule.** No uppercase labels, no letter-spaced labels, no eyebrow or kicker above a heading. A heading says what it introduces.

**The Two Weights Rule.** Headings and footer column titles are 700; buttons, tile names, nav, and the state line are 500; everything else is 400. 600 appears only where a word is picked out inside running text (the "Fits" label, `strong`, store names, the FAQ question).

## Layout

A single 1180px column (`page`) with a fluid gutter of `clamp(1rem, 4vw, 2.5rem)`. Prose pages (FAQ, Where to buy, Contact) narrow to 760px plus gutters. Major sections pad on `band` (`clamp(2.5rem, 6vw, 4.5rem)`); each product group opens 3.5rem below the one before it, and a second row inside a group sits 2.25rem below the first.

- **Header:** a black bar, 76px tall (64px below 760px), in normal flow, not sticky. The floppy mark (2rem) and the wordmark at 1.625rem/700 sit at left, then the nav 2.25rem over with 1.5rem between links. Below 760px a 28px hamburger appears at the far left and the nav becomes a black sheet dropped under the bar, links stacked at 1.0625rem with `bar-divider` rules between them.
- **Hero:** 2.25rem under the bar (1rem below 760px), a two-column box with 4px corners: the lead photo at left, cropped to fill and anchored 30% from the left, and the navy panel at right with the headline, one line, and a white button, vertically centered on a 460px minimum. Below 900px the photo moves above the panel at 4:3 and the panel pads 2.25rem 1.75rem.
- **Product groups:** one `.group` per `params.catalog` entry, in file order: a headline, an optional note in Ink Soft at 60ch, then one 4-up grid of products for sale and, when any product in the group carries a `status`, a second 4-up grid of those. Grids are 4 columns with `2.25rem 1.25rem` gaps; below 900px they go to 2 columns with `1.75rem 1rem` gaps. A short row leaves empty columns at the right rather than stretching; the RS232 group shows two tiles and two empty slots.
- **Product page:** from 900px a two-column grid, `minmax(0, 1.1fr) minmax(320px, 0.9fr)` with a `clamp(2rem, 4vw, 3.5rem)` gap: the plate and thumbnail strip at left, the title, lede, and buy column at right, aligned to the top. A second grid below on the same columns holds the prose at left and the remaining photos at right (one column, or two from 600px when there are more than three). A product with no extra photos (`--solo`) runs its prose in one column. Then "You may also like" in the same 4-up grid, up to four tiles. On phones the order is plate, thumbnails, title, buy column, prose, photos.
- **Where to buy:** store rows 2-up from 640px with 1rem gaps.
- **FAQ:** a hairline-bounded `details` list at the 68ch measure.
- **Footer:** a Tile Gray band from edge to edge, `3rem 0 1.75rem`, holding a `1.2fr 1fr` pair (About at left, "Help and policies" at right as a two-column link list), one column below 900px, then a rule and a centered base line.

Breakpoints observed: 600, 640, 760, 900px. The site collapses almost everything at 900; pick that unless the component already has its own.

### Named Rules
**The Four Across Rule.** Products print four to a row and two on phones, every tile the same width, and a group with fewer than four leaves the rest of the row empty. A third group is one more `[[params.catalog]]` entry and nothing else.

**The Landing Page Rule.** The landing page is the hero and the product groups. About, ordering notes, policies, and store links live in the footer and on their own pages.

## Elevation & Depth

Flat at every state. Nothing casts a shadow, nothing lifts, nothing blurs, and nothing scales. Depth comes from four things only: the black bar against the white page, the navy panel against the photo, the 1px `line` frame around every photo, and the Tile Gray band under the footer. The mobile nav sheet drops over the page as a black panel with a `bar-divider` rule above it and no shadow. Hover is a fill change (buttons, store rows), an underline (links, tile names, nav), or a border color (thumbnails).

The one `box-shadow` in the stylesheets is an inset 1px of Ink on the current product thumbnail, which thickens its frame to 2px without changing its size; it is a border, not an elevation.

### Named Rules
**The Nothing Floats Rule.** No `box-shadow` (except that inset frame), no `filter`, no `backdrop-filter`, no `transform` on hover. If a surface needs to read as separate, give it a 1px `line` border or a Tile Gray fill.

## Shapes

One radius. Every corner on the site is 4px (`base`): the hero box, photo frames, thumbnails, buttons, the label tile, notices, code blocks, store rows, and the "Photo to come" plate. An image inside a label tile and inline code use 3px (`inner`) so they sit inside a 4px parent. Focus rings are 2px of Action Blue at a 3px offset with 2px corners.

Borders are 1px. `line` frames photos, bounds store rows, and rules the buy column, FAQ, tables, and footer base. `ink` borders the secondary button, the table header, and the current thumbnail. Nothing has a 2px border except that thumbnail (via the inset shadow), and nothing is outlined twice.

Drawn marks: the floppy brand mark is an inline SVG, white on the bar, rotated 45°. The hamburger is three 1.6px white strokes; the middle stroke fades when the nav is open. The FAQ chevron is a 0.55rem square with two 1.5px ink borders rotated 45°, turning to point up when open. The "In development" state is an 8px Ink Soft dot. Perk icons are 20px inline SVGs at 1.5px ink stroke, no fill. Store icons are 28px marketplace SVGs from `/img/icons/`.

## Components

### Buttons
Solid and quiet. Inline-flex, label type (500, 0.9375rem, 1.2), padding `0.75rem 1.875rem`, 4px corners, 1px border, 120ms transitions on background, border, and color. No press transform.
- **Primary** (`.btn--primary`): Action Blue fill and border, white text; hover goes to Action Blue Deep. Used full-width (`.btn--block`) in the buy column: "Email about {product}" for an unbuilt product, "Email to order" for a product without a `paypalID`. The only blue surface on the site.
- **Secondary** (`.btn`): white fill, Ink border, Ink text; hover fills Tile Gray Press. The default button for any page that needs one.
- **White** (`.btn--white`): white fill and border, Ink text; hover goes Tile Gray Press on both. Only on the navy hero panel ("See the products"), where a blue button would be a second color.

### Navigation
White links at 0.9375rem/400 on the black bar, `0.375rem` vertical padding, and a 1px bottom border that is transparent at rest, white at 50% on hover (140ms), and solid white on the current page. The catalog entry is current on the home page too. Below 760px the links become a black sheet under the bar: stacked at 1.0625rem with `0.85rem` padding and a `bar-divider` rule under each; the current link goes 600 and loses the white underline.

### Product tile (signature)
A link block with no border, no fill, and no hover lift. A 4:3 `item__media` plate with a 1px `line` frame, 4px corners, and Photo Backing holds the photo cropped to fill. The name sits 0.75rem below at 0.875rem/500, then one Ink Soft line at 0.8125rem that reads "Fits {machines}", plus " · Email to order" when the product has no `paypalID`, or the product's `status` text ("In development") when it has one. Hover underlines the name. A product with `label: true` swaps the plate for a Tile Gray tile with a 10% inset and the printed label shown whole (`object-fit: contain`, 3px corners); a missing image shows "Photo to come" in white on the dark plate.

### Hero panel (signature)
Navy, white text, `3.5rem 3.25rem` padding, flex-column centered on the cross axis, content left-aligned. The `h1` is white at 2.5rem, 14ch max; the line below is white at 92% opacity, 42ch max, 1.125rem under; the white button sits 1.875rem under that. Selection inside the panel inverts to white on navy.

### Buy column (signature)
Not a card: a 1rem-gapped stack under the product lede with no border, no fill, and no padding. In order:
1. **Fits** row at 0.875rem: "Fits" at 600 in Ink, the machines in Ink Soft.
2. Either PayPal's `<paypal-add-to-cart-button>` above a `line` rule (1rem padding), with an optional variant note at 0.9375rem in Ink Soft; or, for a product with `status`, the state line (an 8px Ink Soft dot, the status at 0.875rem/500), "Not for sale yet…" at 0.9375rem in Ink Soft, and a full-width primary button; or, for a product with neither, the unavailable note and a full-width "Email to order" primary button.
3. An underlined guide link, if the product has one; hover goes blue.
4. For a product that is for sale: a `line` rule, then three perks at 0.875rem with 20px ink-stroke icons (ships from San Antonio, 30-day returns, 30-day warranty), then "Also sold on eBay, Tindie, Etsy." at 0.875rem in Ink Soft with underlined Ink links. A product with `status` omits both.

PayPal prints the product's name, price, description, and quantity inside its widget, so the column never repeats them and the site has no price of its own.

### Product plate and thumbnails
The lead photo fills the left column with a 1px `line` frame, 4px corners, and Photo Backing (`fit 1400x1400`); a `label: true` product shows its label at an 8% inset on Tile Gray instead. A caption at 0.875rem in Ink Soft sits 0.5rem below. When the gallery has more than one photo, a strip of 72px thumbnails follows at 0.5rem gaps, each framed in `line`; hover turns the frame Ink Soft (120ms), and the current one gets an Ink frame thickened by the inset shadow. Clicking a thumbnail swaps the plate, its link, and its caption in place.

### Gallery figure
The remaining photos, stacked in the details column at 1.25rem gaps (two across from 600px when more than three), each an 800×600 crop in a `line` frame on Photo Backing, linking to the 1800px original, caption 0.5rem below at 0.875rem in Ink Soft. No hover treatment.

### Store row
A flex row with a 28px marketplace icon, the store name at 600, and an Ink Soft line under it at 0.875rem; white, 1px `line` border, 4px corners, `1.1rem 1.25rem` padding. Hover fills Tile Gray (120ms). The "Direct" row has no icon.

### FAQ row
A `details` list bounded by `line` hairlines at the 68ch measure. The `summary` is 600 at 1rem with `1rem` vertical padding and the drawn ink chevron at the right, rotating from down to up on open over 180ms. Answers are Ink Soft with underlined links and `0.9rem` between paragraphs.

### Notice
A Tile Gray box, 4px corners, `1rem 1.15rem` padding, 0.9375rem at 1.55 in Ink Soft, for an aside inside prose.

### Footer
A Tile Gray band holding two columns: "ArcaneByte" (0.9375rem/700) over the About paragraph from `content/_index.md` at 48ch and a "30-day returns and a 30-day warranty · email" line; and "Help and policies" over a two-column list of page, store, and social links at 0.5rem row gaps. Links are Ink, underlined only in the paragraph; list links underline on hover. Below, a `line` rule and a centered 0.8125rem Ink Soft base line with the year and the location.

### Prose
68ch measure, 1rem between blocks. Links underlined in Ink, blue on hover. `h2` at 1.375rem with 2.25rem above; `h3` at 1.0625rem with 1.5rem above. Lists indent 1.3rem with 0.35rem between items; feature lists under "Features" or "Planned features" are plain bulleted lists. Tables are full-width at 0.9375rem with an Ink rule under the header and `line` rules between rows. Blockquotes carry a 1px `line` left rule and Ink Soft text.

## Do's and Don'ts

### Do:
- **Do** keep blue to the primary button's fill and a link's hover (The One Blue Rule); make every other control white, Ink, or gray.
- **Do** put new content on white; use Tile Gray only for a tile, a notice, a code block, or the footer.
- **Do** use 4px corners on everything, 3px on something nested inside a 4px parent, and 1px `line` frames on every photo.
- **Do** print products four across, two on phones, and leave a short row's empty columns empty.
- **Do** give a product that is not built a `status` in front matter; the second row in its group, the "In development" line, the state dot, the email button, and the "Planned features" heading follow from it.
- **Do** set `label: true` on a product whose only image is its printed label, so the label shows whole on a gray tile.
- **Do** let PayPal's widget print the name, price, and description, and add only what it does not say.
- **Do** show photos in true color on near-black backing, cropped 4:3 in tiles and whole on the product plate.
- **Do** write in American English (catalog, color).

### Don't:
- **Don't** add a second face, a condensed cut, or a monospace label; Inter at normal width is the only type on the site.
- **Don't** set an uppercase or letter-spaced label, or put an eyebrow or kicker above a heading.
- **Don't** cast a shadow, lift, blur, or scale anything at any state; hover is a fill, an underline, or a border color.
- **Don't** add a section to the landing page; it is the hero and the product groups.
- **Don't** publish a price anywhere outside PayPal's widget, and don't invent reviews, counts, or sales figures.
- **Don't** reach for PayPal's yellow or any retro or themed treatment (rules, hatching, typewriter type, period chrome).
- **Don't** make the header sticky or translucent; it is a black bar in normal flow.
