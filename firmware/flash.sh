#!/bin/bash
if [ -z "$1" ]; then
  echo "Available Ports: "
  ls /dev/tty.SLAB_USBtoUART*
  exit 1
fi
PORT=$1
echo "Using $PORT"
esptool.py --port $PORT  erase_flash
esptool.py --port $PORT --baud 460800 write_flash --flash_size=detect 0 adafruit-circuitpython-feather_huzzah-2.2.3.bin
