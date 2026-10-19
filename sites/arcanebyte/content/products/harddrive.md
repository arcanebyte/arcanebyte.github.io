---
title: "Apple Parallel Hard Drive Emulator"
kind: hardware
group: "For the Apple Lisa"
fits: "Apple Lisa, Apple ///"
weight: 60
summary: "A ProFile hard drive emulator for the Apple Lisa and Apple ///, based on Cameo/Aphid."
lede: "Emulates the Apple ProFile hard disk, so a Lisa can boot from an SD card."
image: img/products/harddrive/harddrive1.jpg
unavailableNote: "**Global inventory shortages have impacted availability of the PocketBeagle, which has impacted our ability to build devices.** Please email us to check availability."
aliases:
  - /harddrive-product/
  - /harddrive/
gallery:
  - src: img/products/harddrive/harddrive1.jpg
    caption: "The emulator comes in two versions that support the Apple Lisa and Apple ///"
  - src: img/products/harddrive/harddrive2.jpg
    caption: "The emulator connects straight to the DB25 parallel port on the machine. Pin 7 is removed for compatibility."
  - src: img/products/harddrive/harddrive3.jpg
    caption: "Rev A supports the Apple Lisa 2/5 and Apple ///"
  - src: img/products/harddrive/harddrive4.jpg
    caption: "Rev B supports Apple Lisa 2/5, 2/10 (w/ adapter) and Apple ///"
  - src: img/products/harddrive/harddrive5.jpg
    caption: "The Selector OS for Lisa provides a boot menu for booting from a variety of operating systems on the included SD card"
---

The **Apple Parallel Port Hard Drive Emulator** faithfully emulates the
[Apple ProFile](https://en.wikipedia.org/wiki/Apple_ProFile) series of hard disk drives
introduced in 1981 for the Apple /// Computer and later the Apple Lisa and Macintosh XL.
With little effort, one can install Lisa Office System, MacWorks, SOS, and other
operating systems for the Apple Lisa, Macintosh XL, and Apple ///.

Tom Stepleton, who designed the Cameo/Aphid cape for the PocketBeagle and the associated
software, has graciously donated his efforts to the public domain - so feel free to build
one yourself! Information about the Cameo, Aphid, and Selector can be found at the
following links:

- Cameo: [https://github.com/stepleton/cameo](https://github.com/stepleton/cameo)
- Aphid: [https://github.com/stepleton/cameo/tree/master/aphid](https://github.com/stepleton/cameo/tree/master/aphid)
- Selector: [https://github.com/stepleton/cameo/tree/master/aphid/selector](https://github.com/stepleton/cameo/tree/master/aphid/selector)

The emulator is a Linux-based system that works by presenting a disk image file as an
Apple ProFile hard drive to the connected system. It supports 5MB and 10MB "ProFile"
disk sizes, as well as arbitrary sizes for operating systems that support it (i.e.
MacWorks).

## Revisions

There are two variants of this product. Choose 'Rev A' or 'Rev B' at checkout.

- **Revision A**: Supports Apple Lisa 2/5 and Apple ///
- **Revision B**: Supports Apple Lisa 2/5, Apple Lisa 2/10, and Apple ///

Both Rev A and Rev B designs have been made available for
[download](https://github.com/stepleton/cameo/tree/master/hardware/arcanebyte_aphde) in
EAGLE format should you choose to build one yourself.

## What's included

At this time, all **Apple Parallel Port Hard Drive Emulator** devices sold by ArcaneByte
are sold as a completed kit that include the emulator, adapter board, SD card with
pre-installed disk images (Lisa Only), and a MicroUSB power cable. For Lisa 2/10
systems, a Widget adapter is recommended (sold separately).

{{< notice >}}
Global inventory shortages have impacted availability of the PocketBeagle, which has
impacted our ability to build devices. Please email us to check availability.
{{< /notice >}}
