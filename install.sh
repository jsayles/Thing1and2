#!/bin/bash

# Activate python environment
source .venv/bin/activate

# A POSIX variable
# Reset in case getopts has been used previously in the shell.
OPTIND=1

# Defaults
PORT="/dev/tty.SLAB_USBtoUART"
FLASH=0
MODE="direct"

function show_help {
  echo "Install CircutePython to Feather"
  echo " -p <port>:  Use specified port ($PORT) "
  echo " -m <mode>:  Uplaod specified mode ($MODE) "
  echo " -f:  Flash before uploading files"
}

# Parse the command line args
while getopts ":h:p:m:f:" opt; do
    case $opt in
    (p) PORT=$OPTARG;;
    (m) MODE=$OPTARG;;
    (:)
      case $OPTARG in
        (f) FLASH=1;;
        (h)
            show_help
            exit 0;;
      esac;;
    esac
done
echo "Mode: '$MODE', Port: $PORT"

# Optionally flash the firmeware
if [ "$FLASH" == 1 ]; then
  echo "Flashing the firmware..."
  cd firmware
  ./flash.sh $PORT
  cd - > /dev/null
  echo "Waiting for reboot..."
  sleep 4
fi

function upload {
  SRC_FILE=$1
  DEST_FILE=$SRC_FILE
  if [[ -n "$2" ]]; then
    DEST_FILE=$2;
    echo -n "Uploading $SRC_FILE to $DEST_FILE..."
  else
    echo -n "Uploading $SRC_FILE..."
  fi
  ampy -p $PORT put $SRC_FILE $DEST_FILE
  echo
}

# Main Functions
echo "Uploading the source files..."
cd src
upload settings.py
upload utils.py
upload core.py
upload thingnet.py
upload $MODE.py main.py
cd - > /dev/null
