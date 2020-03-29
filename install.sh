#!/bin/bash

# Activate python environment
source .venv/bin/activate

if [ -z "$1" ]; then
  PORT="/dev/tty.SLAB_USBtoUART"
else
  PORT=$1
fi
echo "Using $PORT"

function upload {
  SRC_FILE=$1
  echo -n "Uploading $SRC_FILE..."
  ampy -p $PORT put $SRC_FILE
  echo
}

if [ "$2" == "-f" ]; then
  echo "Flashing the firmware..."
  cd firmware
  ./flash.sh $PORT
  cd - > /dev/null
  echo "Waiting for reboot..."
  sleep 4
fi

#for i in *.py;
#do
#   echo "Uploading $i...";
#   ampy -p /dev/tty.SLAB_USBtoUART put $i;
#done

echo "Uploading the source files..."
cd src
upload settings.py
upload utils.py
upload core.py
upload main.py
cd - > /dev/null
