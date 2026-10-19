---
title: "LisaBoost"
kind: hardware
group: "For the Apple Lisa"
fits: "Apple Lisa"
weight: 80
summary: "A faster 68000 and up to 32 MB of memory"
lede: "A processor and memory card for the Lisa. Model No. LB101."
image: img/products/lisaboost/label.png
label: true
status: "In development"
specs:
  - "Plugs into the 68000 socket on the Lisa CPU board, in place of the processor"
  - "Speed steps of 9.38, 12.5, 18.75, and 37.5 MHz"
  - "32 MB of memory on the card"
  - "MacWorks Plus II 2.5.0 finds the extra memory with no patch"
  - "Starts in stock mode, so the Office System, Workshop, and Xenix see an ordinary Lisa"
  - "Card Setup at power-on, saved in flash, with a safe mode and floppy firmware updates"
---

LisaBoost replaces the Lisa's 68000 with a cycle-exact 68000 running in an FPGA, alongside
32 MB of memory and 4 MB of flash. It drops into the processor socket on the CPU board,
so nothing about the Lisa needs to change.

At power-on the card behaves like a stock Lisa. Card Setup lets you pick a faster speed and
how much memory to show. MacWorks Plus II sees up to 8 MB through its built-in XLerator
support and can use the rest as a RAM disk. UniPlus, with a patched kernel, can use up to 16 MB.

## Status

The Rev A board is designed and nothing has been built yet. Everything above has been
tested in simulation and in the LisaEm emulator, not yet on a real Lisa. There's no price
yet.
