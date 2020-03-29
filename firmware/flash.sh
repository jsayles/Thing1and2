#!/bin/bash

# Activate python environment
source ../.venv/bin/activate

if [ -z "$1" ]; then
  PORT="/dev/tty.SLAB_USBtoUART"
else
  PORT=$1
fi
echo "Using $PORT"

esptool.py --port $PORT  erase_flash
# esptool.py --port $PORT --baud 460800 write_flash --flash_size=detect 0 adafruit-circuitpython-feather_huzzah-*.bin
esptool.py --port $PORT --baud 460800 write_flash --flash_size=detect 0 adafruit-circuitpython-feather_huzzah-3.1.2.bin
