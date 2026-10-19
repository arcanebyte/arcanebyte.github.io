# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Owners and restorers of vintage computers, mostly the Apple Lisa, Macintosh XL, and
Apple ///. Some buyers are general retro hobbyists with an RS232 serial port (the WiFiModem
range). They arrive from eBay, Tindie, Etsy, forums, and YouTube, often through a link to
one product. They want to know what fits their machine, see photos of the real thing, and
buy it.

## Product Purpose

ArcaneByte is a small maker shop in San Antonio, Texas, established in 2018. It sells
hand-built hardware for machines the manufacturer stopped supporting decades ago:
keyboard adapters (adb2lisa, usb2lisa, mac2lisa), a ProFile hard drive emulator (the
Apple Parallel Hard Drive Emulator), and WiFi modems (WiFiModem, WiFiModem32).
The site counts as a success when a visitor finds the right part, believes it is real and
well made, and checks out.

## Positioning

Hardware that makes Lisa-era machines usable again, built by one shop that knows these
machines closely. The range is broader than adapters. Headline: "Goodies for machines
nobody supports."

## Operating Context

- Checkout is PayPal's hosted cart (`cart.js`, loaded blocking in `<head>`). Each product
  has a `paypalID` in its front matter.
- The same products are also sold on eBay, Tindie, and Etsy.
- Each product page has photos, a spec list, and compatibility notes.
- Returns and warranty are both 30 days.
- The shop also offers OpenStack and network consulting. The `/consulting/` page is hidden for now.

## Capabilities and Constraints

- Static Hugo site in `sites/arcanebyte`, using the `themes/base` theme. Served by nginx
  in Docker.
- Product photos are resized at build time from `assets/img/products/`.
- Old Jekyll URLs must keep redirecting through `aliases`.
- Cloudglass (the OpenStack dashboard) has been removed from the business's web
  presence (2026-10-12).

## Brand Commitments

- Name: ArcaneByte (shown as "Arcane" + "Byte").
- The owner wants the design simpler and more retro.
- Standing preference (2026-10-17): the conventional storefront layout, done at full craft.
  The owner was shown four period-specific directions (annotated brochure, Lisa Office
  System desktop, HyperCard stack, build-instruction booklet) and chose the category
  standard instead. Don't re-pitch a themed world; make the familiar layout excellent.
- Reference and shape (2026-10-18): the owner asked for a mockup "along the lines of"
  shop.bigmessowires.com and chose it over a paper parts catalog, a dark workbench, an
  apple.com-style lineup, and a serif magazine layout. Then: "everything we have today is
  for Lisa or is a RS232 modem. we might have more later. the main landing page is just
  busy." So the landing page is only the hero and the product groups. No machine picker,
  no About or ordering notes on the landing page (those live in the footer and on their
  own pages). Products are grouped by what they are for ("For the Apple Lisa", "For
  anything with an RS232 serial port"), with unbuilt cards in a second row of their
  group, and a new group is one more `[[params.catalog]]` entry.

## Evidence on Hand

- Real product photos in `sites/arcanebyte/assets/img/products/<name>/`.
- WiFiModem quick-start guide PDF in `static/guides/`.
- FAQ content in `data/faq.yaml`.
- There are no testimonials, review counts, or sales figures. Don't invent any.

## Product Principles

1. The real hardware is the hero. Show the actual photos and the actual specs.
2. Lead with compatibility: which machine is this for?
3. Checkout must never break, so the PayPal cart and the store links stay working.
4. Write like a person at a bench, not a corporation.
