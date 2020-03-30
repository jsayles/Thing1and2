# Thing 1 and Thing 2
An overly simplistic set of communication devices: Thing1 and Thing2.
You press the button on Thing1 and the light/haptic on Thing2 is triggered.  Same is true the other way around.  

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

* CircuitPython 3.1.2:  https://circuitpython.readthedocs.io/en/3.x/README.html
* CircuitPython for ESP8266: https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266
* **System Documetation**: [docs/main.md](docs/main.md)

## Tutorials

* HUZZAH Pinouts: https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/pinouts
* Haptic Controller: https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/circuitpython-code
* LED Circuit: https://learn.adafruit.com/remote-control-with-the-huzzah-plus-adafruit-io/monitor-wiring

## USB Drivers

You need to install the CP2104 USB drivers in order to interact with the huzzah feather.  

https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide
http://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

## Python Environment Install

```
python3 -m venv .venv
source .venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## Userful Commands
Enter the REPL:  
```
screen /dev/tty.SLAB_USBtoUART 115200
```

List files on the feather.  (With the .ampy file you don't need to specify the port):
```
ampy --port /dev/tty.SLAB_USBtoUART ls
```

Erase the feather:  
```
esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
```

## Useful Links

* Adafruit Ampy Tool:  
  * https://github.com/scientifichackers/ampy
  * https://learn.adafruit.com/micropython-basics-load-files-and-run-code/
