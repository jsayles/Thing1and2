#!/bin/bash
source bin/activate
cd src
for i in *.py;
do
   echo "Uploading $i...";
   ampy -p /dev/tty.SLAB_USBtoUART put $i;
done
