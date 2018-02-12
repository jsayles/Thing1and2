#!/bin/bash
esptool.py --port /dev/tty.SLAB_USBtoUART  erase_flash
esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 adafruit-circuitpython-feather_huzzah-2.2.3.bin
