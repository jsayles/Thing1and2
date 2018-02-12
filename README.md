# Thing 1 and Thing 2
An overly simplistic set of communication devices

## REPL
```screen /dev/tty.SLAB_USBtoUART 115200```

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

## Tutorials

* HUZZAH Pinouts: https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/pinouts
* Haptic Controller: https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/circuitpython-code
* LED Circuit: https://learn.adafruit.com/remote-control-with-the-huzzah-plus-adafruit-io/monitor-wiring

## TODO

* Wire up button - use interrupts
* Wire up haptic Board
* Wire up power switch - Connect EN to Ground
