# arcanebyte.com

A static site built with [Hugo](https://gohugo.io/) on one base theme, served by nginx.

| site | directory | production URL |
|---|---|---|
| ArcaneByte — hardware and software | `sites/arcanebyte` | https://www.arcanebyte.com |

There is no Ruby, no Node, and no `node_modules`. Hugo is a single binary and the only
build dependency.

## Layout

```
themes/base/            shell: baseof, head, header, footer, 404, tokens + typography
  assets/css/base.css   design tokens, layout, the header bar, buttons, prose, footer
  static/fonts/         Inter, self-hosted
sites/arcanebyte/       the shop
  assets/css/site.css   shop CSS (hero, product groups and tiles, product page, stores)
  assets/img/products/  product photos, resized at build time
  content/products/     one markdown file per product
  layouts/              home, products, faq, purchase, catalog groups, and the buy column
  data/faq.yaml         FAQ questions and answers
deploy/                 Dockerfile and nginx.conf
scripts/check_output.py link and image checker
```

Anything the site does not define falls back to `themes/base`. To override a theme
template, put the same path inside `sites/arcanebyte/layouts/`.

## Local development

```bash
brew install hugo      # or see gohugo.io/installation

make dev               # http://127.0.0.1:1313
```

```bash
make build             # into dist/
make check             # build, then fail on broken links or missing images
```

## Running it

```bash
docker compose up --build
#   arcanebyte -> http://localhost:8090
```

nginx serves the site on `:80` and redirects the apex domain to `www`. TLS is expected to terminate upstream, which is why
nothing in `deploy/nginx.conf` listens on 443.

## Adding a product

Run `make product name=<name>`. It creates `sites/arcanebyte/content/products/<name>.md`
from a filled-in template, plus an empty `assets/img/products/<name>/` folder for photos.
The fields look like this:

```yaml
---
title: "widget2lisa"
kind: hardware
group: "For the Apple Lisa" # a group name from params.catalog in hugo.toml
fits: "Apple Lisa, Macintosh XL"
weight: 80                  # ordering within its group
summary: "One line for the catalog listing."
lede: "One sentence under the page title."
image: img/products/widget2lisa/hero.jpg
label: true                 # image is the printed label: shown whole on a gray tile
status: "In development"    # not for sale yet: no order form, second row of its group
paypalID: "XXXXXXXXXXXXX"   # omit for no direct checkout
variantNote: "Choose 'male' or 'female' at checkout."
specs:
  - "A bullet in the spec list"
gallery:
  - src: img/products/widget2lisa/one.jpg
    caption: "What this photo shows"
---

Body copy in markdown.
```

Photos go in `sites/arcanebyte/assets/img/products/<name>/` — **not** `static/`. Being
in `assets/` is what lets Hugo resize them at build time. Front-matter image paths are
relative to `assets/`, so they have no leading slash.

Nothing else needs editing. The listing, the "You may also like" row on each product
page, and the sitemap all come from front matter. Within a group, products for sale
print first and anything with a `status` prints in a second row. To add a group (say,
for a new machine), add a `[[params.catalog]]` entry in `hugo.toml` with a `name` and an
optional `note`; groups print in that order on the home page and on `/products/`.

## PayPal

Checkout is PayPal's hosted "no-code" cart.

- The merchant ID is `params.paypal.merchantID` in `sites/arcanebyte/hugo.toml`.
- Each product's button ID is `paypalID` in its front matter.
- `cart.js` is loaded **blocking, in `<head>`**, site-wide. It has to load before the
  per-product `cartPaypal.AddToCart(...)` call that the buy box emits in the body, and
  the cart persists across pages. Deferring it breaks checkout.
- The widget renders its own product name, price, description and quantity from PayPal,
  so the buy box deliberately adds only what PayPal does not say.

## Images

Product photos are 2–9 MB straight off the camera. Hugo resizes them at build time:
listings are cropped to 4:3 with the `Smart` (entropy) anchor and sharpened, gallery
thumbnails likewise, and each gallery photo links to an uncropped 1800px version. Output
is WebP.

The homepage ships about 225 KB of images instead of the ~10 MB the originals would be.
Colors are left true — these are product photos, and the adapters are sold in specific
colors.

## Old URLs

The Jekyll site used `/adb2lisa-product/`. Those paths are `aliases` in each product's
front matter, so Hugo emits redirects and existing links from eBay, Tindie and Etsy
listings keep working.
