---
layout: post
title: Parallel Hard Drive Emulator for Apple Lisa and Apple ///
category:
    columns: 4
---

### Description

The **Apple Parallel Port Hard Drive Emulator** faithfully emulates the [Apple ProFile](https://en.wikipedia.org/wiki/Apple_ProFile) series of hard disk drives introduced in 1981 for the Apple /// Computer and later the Apple Lisa and Macintosh XL. With little effort, one can install Lisa Office System, MacWorks, SOS, and other operating systems for the Apple Lisa, Macintosh XL, and Apple ///.

Tom Stepleton, who designed the Cameo/Aphid cape for the PocketBeagle and the associated software, has graciously donated his efforts to the public domain - so feel free to build one yourself! Information about the Cameo, Aphid, and Selector can be found at the following links:

Cameo: [https://github.com/stepleton/cameo](https://github.com/stepleton/cameo)
Aphid: [https://github.com/stepleton/cameo/tree/master/aphid](https://github.com/stepleton/cameo)
Selector: [https://github.com/stepleton/cameo/tree/master/aphid/selector](https://github.com/stepleton/cameo)

The emulator is a Linux-based system that works by presenting a disk image file as an Apple ProFile hard drive to the connected system. It supports 5MB and 10MB "ProFile" disk sizes, as well as ardbitrary sizes for operating systems that support it (MacWorks).

The **Apple Parallel Port Hard Drive Emulator** has been made available for sale by ArcaneByte with limited support. There are two variants of this product. Choose 'Rev A' or 'Rev B' at checkout.

- Revision A: Supports Apple Lisa 2/5 and Apple ///
- Revision B: Supports Apple Lisa 2/5, Apple Lisa 2/10, and Apple ///

At this time, all **Apple Parallel Port Hard Drive Emulator** devices sold by ArcaneByte are sold as a completed kit that include the emulator, adapter board, SD card with pre-installed disk images (Lisa Only), and a MicroUSB power cable. For Lisa 2/10 systems, a Widget adapter is recommended (sold seperately).

<div id="smart-button-container">
      <div style="text-align: center;">
        <div style="margin-bottom: 1.25rem;">
          <p>Apple Parallel Hard Drive Emulator</p>
          <select id="item-options"><option value="Revision A" price="119.95">Revision A Kit - 119.95 USD</option><option value="Revision B" price="149.95">Revision B Kit cancel.md- 149.95 USD</option><option value="Widget Adapter Cable" price="12.95">Widget Adapter Cable - 12.95 USD</option></select>
          <select style="visibility: hidden" id="quantitySelect"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option></select>
        </div>
      <div id="paypal-button-container"></div>
      </div>
    </div>
<script src="https://www.paypal.com/sdk/js?client-id=AWLPOcvu-HQoswvT8u4kEd2eJoeNfIrv1Qn75bweyuse9A-UM35n6hhVfbbrEmHuruRLo-68ixbkCDPM&enable-funding=venmo&currency=USD" data-sdk-integration-source="button-factory"></script>
<script>
      function initPayPalButton() {
        var shipping = 5.95;
        var itemOptions = document.querySelector("#smart-button-container #item-options");
    var quantity = parseInt(5);
    var quantitySelect = document.querySelector("#smart-button-container #quantitySelect");
    if (!isNaN(quantity)) {
      quantitySelect.style.visibility = "visible";
    }
    var orderDescription = 'Apple Parallel Hard Drive Emulator';
    if(orderDescription === '') {
      orderDescription = 'Item';
    }
    paypal.Buttons({
      style: {
        shape: 'pill',
        color: 'gold',
        layout: 'vertical',
        label: 'paypal',
        
      },
      createOrder: function(data, actions) {
        var selectedItemDescription = itemOptions.options[itemOptions.selectedIndex].value;
        var selectedItemPrice = parseFloat(itemOptions.options[itemOptions.selectedIndex].getAttribute("price"));
        var tax = (0 === 0 || false) ? 0 : (selectedItemPrice * (parseFloat(0)/100));
        if(quantitySelect.options.length > 0) {
          quantity = parseInt(quantitySelect.options[quantitySelect.selectedIndex].value);
        } else {
          quantity = 1;
        }

        tax *= quantity;
        tax = Math.round(tax * 100) / 100;
        var priceTotal = quantity * selectedItemPrice + parseFloat(shipping) + tax;
        priceTotal = Math.round(priceTotal * 100) / 100;
        var itemTotalValue = Math.round((selectedItemPrice * quantity) * 100) / 100;

        return actions.order.create({
          purchase_units: [{
            description: orderDescription,
            amount: {
              currency_code: 'USD',
              value: priceTotal,
              breakdown: {
                item_total: {
                  currency_code: 'USD',
                  value: itemTotalValue,
                },
                shipping: {
                  currency_code: 'USD',
                  value: shipping,
                },
                tax_total: {
                  currency_code: 'USD',
                  value: tax,
                }
              }
            },
            items: [{
              name: selectedItemDescription,
              unit_amount: {
                currency_code: 'USD',
                value: selectedItemPrice,
              },
              quantity: quantity
            }]
          }]
        });
      },
      onApprove: function(data, actions) {
        return actions.order.capture().then(function(orderData) {
          
          // Full available details
          console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

          // Show a success message within this page, e.g.
          const element = document.getElementById('paypal-button-container');
          element.innerHTML = '';
          element.innerHTML = '<h3>Thank you for your payment!</h3>';

          // Or go to another URL:  actions.redirect('thank_you.html');

        });
      },
      onError: function(err) {
        console.log(err);
      },
    }).render('#paypal-button-container');
  }
  initPayPalButton();
</script>
    
{% include image.html img="wifimodem/wifimodem1.jpg" lightbox="true" alt="wifimodem" caption="wifimodem comes in male or female version" width="400" class="center" %}
