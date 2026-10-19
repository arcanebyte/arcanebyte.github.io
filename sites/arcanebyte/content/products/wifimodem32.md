---
title: "WiFiModem32"
kind: hardware
group: "For anything with an RS232 serial port"
fits: "Any machine with an RS232 serial port"
weight: 50
summary: "ESP32-based wireless modem for vintage computers, with SSH support."
lede: "The same idea as the WiFiModem, on a chipset with more room to work."
image: img/products/wifimodem/wifimodem3.jpg
paypalID: "RPFPUB6WAG8NL"
variantNote: "There are two variants of this product. Choose 'male' or 'female' connector at checkout."
guide:
  name: "Download the Quick Start Guide (PDF)"
  url: /guides/wifimodem_qsg_1.4.pdf
aliases:
  - /wifimodem32-product/
  - /wifimodem32/
gallery:
  - src: img/products/wifimodem/wifimodem3.jpg
    caption: "the modem with a male connector"
  - src: img/products/wifimodem/wifimodem2.jpg
    caption: "the modem with a female connector"
  - src: img/products/wifimodem/wifimodem5.jpg
    caption: "connected to a Macintosh SE"
  - src: img/products/wifimodem/wifimodem8.jpg
    caption: "connected to an Apple Lisa running UNIX"
---

Retro is cosmo, again! The ArcaneByte WiFiModem32 is a Hayes-compatible wifi modem for
vintage computers with an RS232 serial port that can be used to connect to
Internet-based resources.

With the WiFiModem32, you can connect to your favorite Internet-based BBS using an IP
address rather than a phone number. Transfer files using zmodem or Kermit @ 1200 baud
for that true vintage experience. If you want to host a BBS, enable the TCP/IP listener
function to 'dial in' to your retro machine. The possibilities really are endless!

The ArcaneByte WiFiModem32 is a hand-built device that utilizes firmware authored by Bo
Zimmerman (available on Github) and an ESP32-based chipset. With the Arduino IDE you are
free to install any firmware you see fit. The device is powered by a USB-C cable and
requires 5V to operate. Connect the WiFiModem32 directly to your DB25 serial port, or
use a straight-through extension cable and/or DB9 adapter and/or gender changer, if
necessary. Supports common baud rates (300, 1200, 2400, 4800, 9600, 19200+).

The ESP32 chipset offers more functionality over the ESP8266 chipset used in previous
variants, and can support SSH and other functionality baked into Zimodem.

## Quick start guide

For assistance in setting up the WiFiModem32, download the Quick Start Guide
[here](/guides/wifimodem_qsg_1.4.pdf).
