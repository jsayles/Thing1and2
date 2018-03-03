#!/bin/bash
source bin/activate

if [ -z "$1" ]; then
  echo "Available Ports: "
  ls /dev/tty.SLAB_USBtoUART*
  exit 1
fi
PORT=$1
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
upload core.py
upload settings.py
upload main.py
# upload utils.py
# upload thingnet.py
# upload thing1.py
# upload thing2.py
cd - > /dev/null
