# Thing 1 and Thing 2
An overly simplistic set of communication devices: Thing1 and Thing2

## Userful Commands
```screen /dev/tty.SLAB_USBtoUART 115200```
```ampy --port /dev/tty.SLAB_USBtoUART ls```

## Hardware

* Adafruit Feather HUZZAH ESP8266: https://www.adafruit.com/product/2821
* Adafruit DRV2605 Haptic Controller Breakout: https://www.adafruit.com/product/2305
* Vibrating Mini Motor Disc: https://www.adafruit.com/product/1201
* FeatherWing Prototyping Board: https://www.adafruit.com/product/2884
* Square Buttons: https://www.adafruit.com/product/1010
* RGB LED: https://www.adafruit.com/product/848
* Lithium Ion Polymer Battery: https://www.adafruit.com/product/1578

## Pins

* 2 = Button
* 4,5 = I2C Buzzer
* 12 = Blue led
* 13 = Green led
* 16 = Red led

## Software

* Circuit Python 2.2.3
* CircuitPython for ESP8266: https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266

## Identity

For this code to work thing1 and thing2 need to know who they are and which
role they are playing.  To do this their individual mac addresses are set in
settings.py which checks the mac and sets I_AM_THING1 and I_AM_THING2 accordingly.

## Tutorials

* HUZZAH Pinouts: https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/pinouts
* Haptic Controller: https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/circuitpython-code
* LED Circuit: https://learn.adafruit.com/remote-control-with-the-huzzah-plus-adafruit-io/monitor-wiring

## USB Drivers

You need to install the CP2104 USB drivers in order to interact with the huzzah feather.  

https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide
http://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

## TODO

* Make LED class to abstract all LEDs
* Use PWM to dim power LED
* Use main LED for network status
