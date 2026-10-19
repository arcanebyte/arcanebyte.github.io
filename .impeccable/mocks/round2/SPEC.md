# Round 2 mockups: shared packet

Four alternative homepage designs for ArcaneByte, built as self-contained static HTML mockups so the owner can compare them against the storefront now live at http://localhost:1313/ (captured at `.impeccable/review/desktop.png`).

## Rules for every mockup

- One file per direction: `.impeccable/mocks/round2/<id>.html`. Self-contained CSS in a `<style>` block. No JS needed beyond, at most, a mobile nav toggle.
- Do not touch anything under `sites/` or `themes/`. Only write inside `.impeccable/mocks/round2/`.
- Images: reference the real photos by relative path from the mockup file, e.g. `../../../sites/arcanebyte/assets/img/products/adb2lisa/adb2lisa4.jpg`. Use `object-fit` to crop. Big files are fine; this is a mockup.
- Fonts: Archivo variable is self-hosted at `../../../themes/base/static/fonts/archivo-var-latin.woff2` (`@font-face { font-family: Archivo; src: url(...) format("woff2"); font-weight: 100 900; }`). Google Fonts are allowed for a direction's own face (the network works). Never use `font-stretch` other than 100%. No condensed or extended faces; the owner found them "stretched."
- Full homepage, real content, American English. The page must contain, in whatever order and form the direction dictates:
  - Header with the brand and nav: Catalog, Where to buy, FAQ, Contact.
  - Headline "Goodies for machines nobody supports." Lede: "Hand-built adapters, modems, and drive emulators for the Apple Lisa, Macintosh XL, and Apple ///."
  - Some way to find products by machine: Apple Lisa (adb2lisa, mac2lisa, usb2lisa, Apple Parallel Hard Drive Emulator), Macintosh XL (adb2lisa, mac2lisa, usb2lisa), Apple /// (Apple Parallel Hard Drive Emulator), Anything with an RS232 port (WiFiModem, WiFiModem32).
  - The catalog in four groups, in this order, with these blurbs and products:
    1. Keyboard adapters. "Use a USB, ADB, or original Macintosh keyboard on a Lisa or Macintosh XL."
       - adb2lisa. "Connects Apple Desktop Bus (ADB) keyboards to the Apple Lisa and Macintosh XL." Fits Apple Lisa, Macintosh XL. Photo adb2lisa/adb2lisa4.jpg (red and white pair on black leatherette, 2947x1500). Orderable (PayPal).
       - mac2lisa. "Connects Macintosh 128k/512k/Plus keyboards to the Apple Lisa and Macintosh XL." Fits Apple Lisa, Macintosh XL. Photo mac2lisa/mac2lisa4.jpg (black board, 721x866 portrait). Orderable.
       - usb2lisa. "Connects Universal Serial Bus (USB) keyboards to the Apple Lisa and Macintosh XL." Fits Apple Lisa, Macintosh XL. Photo usb2lisa/usb2lisa1.jpg (board with yellow cable on black, 4032x3024). Email to order.
    2. Modems. "Put a machine with an RS232 serial port on WiFi, and dial a BBS by IP address."
       - WiFiModem. "ESP8266-based wireless modem for vintage computers with an RS232 serial port." Fits any machine with an RS232 serial port. Photo wifimodem/wifimodem1.jpg (two modems on black, 3842x1865). Orderable, male or female connector.
       - WiFiModem32. "ESP32-based wireless modem for vintage computers, with SSH support." Same fit. Photo wifimodem/wifimodem3.jpg (one modem on black). Orderable.
    3. Hard drive emulators. "Stand in for an Apple ProFile hard disk, using disk image files."
       - Apple Parallel Hard Drive Emulator. "A ProFile hard drive emulator for the Apple Lisa and Apple ///, based on Cameo/Aphid." Fits Apple Lisa, Apple ///. Photo harddrive/harddrive1.jpg (two boards on black, 4032x2219). Email to order.
    4. In the workshop. "Cards for the Lisa that are designed but not built yet." All four are "In development", no price, no order button. Their picture is a printed label (cream paper with a purple band, 2007x1299), at `<slug>/label.png`:
       - LisaBoost (LB101). "A faster 68000 and up to 32 MB of memory"
       - Apple IIe Card (A2E101). "A real 65C02 and the enhanced IIe's ROMs on a card so the Lisa can run Apple II software."
       - LisaColor (LC101). "A video card that gives MacWorks a 16-color desktop on a modern display."
       - LisaLink (EN101). "An Ethernet and WiFi card that puts the Lisa on a modern network."
  - How to order: Here (most products have a PayPal order form on their page), Marketplaces (eBay, Tindie, Etsy), Direct (email support@arcanebyte.com for an invoice). 30-day returns and a 30-day warranty.
  - About: "ArcaneByte was established in 2018 as a maker in the vintage computing space. We specialize particularly in the Apple Lisa and Macintosh XL, but offer a variety of gadgets that are compatible with other vintage systems." San Antonio, Texas.
  - Footer with the groups, Buying (Where to buy, FAQ, eBay), ArcaneByte (Contact, YouTube, GitHub).
- No prices anywhere (none are published). No invented testimonials, press quotes, stock counts, ratings, or claims. Buttons say "Order", "Email to order", or show "In development".
- Craft floor (hard rules): no kicker or eyebrow labels above headings; no section numbers; no gradient text; no glass or blur as decoration; no thick colored left borders; no hard offset shadows; no monospace as a "technical" costume (a model number may be set in small caps or tabular figures instead); no emoji or Unicode glyphs as icons (draw any icon as inline SVG); body text contrast at least 4.5:1; body measure 65 to 75 characters; headings balanced (`text-wrap: balance`); one accent color used for actions only unless the direction says otherwise; style `::selection`, `:focus-visible`, and link underline offset from the palette; hover states on every link and card; `prefers-reduced-motion` respected if anything moves.
- Responsive: must hold at 500px wide (the narrowest headless Chrome can capture on this Mac) and at 1440px. 16px minimum side gutter on phones, no horizontal scroll.

## Capture

After writing the file, capture it twice with headless Chrome and look at both captures once, fix what they show in one batch, and recapture once. Two rounds is the ceiling.

```
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cd /Users/jdenton/github/arcanebyte.github.io/.impeccable/mocks/round2
"$C" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,3600 --virtual-time-budget=6000 --screenshot=<id>.png "file://$PWD/<id>.html"
"$C" --headless=new --disable-gpu --hide-scrollbars --window-size=500,5200 --virtual-time-budget=6000 --screenshot=<id>-phone.png "file://$PWD/<id>.html"
```

If the page is shorter than the window, trim the blank bottom with `sips -c <height> 1440 <id>.png` (height first) so the comp has no dead space; if it is longer, that's fine, the comp shows the top.

Report back in under 150 words: the two file paths, what the first viewport shows, and anything you could not do.
