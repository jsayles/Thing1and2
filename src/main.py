#####################################################################
# Functions to operate the RGB led
#
# Note:  LED is wired high so bring led pin low to turn on.
#####################################################################

import time
import machine


red_led = machine.Pin(16, machine.Pin.OUT)
blue_led = machine.Pin(12, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

i = 1
while(True):
    red_led.on()
    blue_led.on()
    green_led.on()
    if i == 1:
        red_led.off()
    elif i == 2:
        blue_led.off()
    else:
        green_led.off()
        i = 0
    time.sleep(1)
    i = i + 1



# Start with the led off
#led_off()


def led_off():
    red_led.on()
    blue_led.on()
    green_led.on()


def led_red():
    red_led.off()
    blue_led.on()
    green_led.on()


def led_blue():
    red_led.on()
    blue_led.off()
    green_led.on()


def led_green():
    red_led.on()
    blue_led.on()
    green_led.off()


def led_white():
    red_led.off()
    blue_led.off()
    green_led.off()


def led_yellow():
    red_led.on()
    blue_led.off()
    green_led.off()


def led_orange():
    red_led.off()
    blue_led.on()
    green_led.off()


def led_purple():
    red_led.off()
    blue_led.off()
    green_led.on()
