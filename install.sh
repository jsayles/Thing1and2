#!/bin/bash

source bin/activate

cd src
ampy --port /dev/tty.SLAB_USBtoUART put *
