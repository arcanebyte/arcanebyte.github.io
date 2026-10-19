---
title: "{{ .File.ContentBaseName }}"
kind: hardware
# A group name from params.catalog in hugo.toml. Something not for sale yet
# stays in its group and gets `status` below instead.
group: "For the Apple Lisa"
fits: "Apple Lisa, Macintosh XL"
weight: 100                 # ordering on the page, lower comes first
summary: "One line for the catalog listing."
lede: "One sentence under the page title."
# Put photos in assets/img/products/{{ .File.ContentBaseName }}/
image: img/products/{{ .File.ContentBaseName }}/hero.jpg
# label: true               # if the image is the printed label, show it whole
# status: "In development"  # not for sale yet: no order form
# The button ID from PayPal (Pay Links & Buttons > Add to cart). Leave it out
# and the page says "Email to order".
paypalID: ""
# variantNote: "Choose 'male' or 'female' at checkout."
specs:
  - "A feature"
gallery:
  - src: img/products/{{ .File.ContentBaseName }}/hero.jpg
    caption: "What this photo shows"
---

What it is and what it does, in a paragraph or two.
