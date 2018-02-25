#!/bin/bash
source bin/activate

echo "Flashing the firmware..."
cd firmware
./flash.sh
cd -

#for i in *.py;
#do
#   echo "Uploading $i...";
#   ampy -p /dev/tty.SLAB_USBtoUART put $i;
#done

echo "Uploading the source files..."
cd src
ampy -p /dev/tty.SLAB_USBtoUART put settings.py
ampy -p /dev/tty.SLAB_USBtoUART put utils.py
ampy -p /dev/tty.SLAB_USBtoUART put led.py
ampy -p /dev/tty.SLAB_USBtoUART put vibe.py
ampy -p /dev/tty.SLAB_USBtoUART put thingnet.py
ampy -p /dev/tty.SLAB_USBtoUART put thing1.py
ampy -p /dev/tty.SLAB_USBtoUART put thing2.py
cd -

