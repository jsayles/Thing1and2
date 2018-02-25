#####################################################################
# Functions to operate the RGB led
#
# Note:  LED is wired high so bring led pin low to turn on.
#####################################################################

import time
import settings
import machine


def off():
    settings.red_led.on()
    settings.blue_led.on()
    settings.green_led.on()

def red_on():
    settings.red_led.off()

def red_off():
    settings.red_led.on()

def red():
    off()
    red_on()

def green_on():
    settings.green_led.off()

def green_off():
    settings.green_led.on()

def green():
    off()
    green_on()

def blue_on():
    settings.blue_led.off()

def blue_off():
    settings.blue_led.on()

def blue():
    off()
    blue_on()

def white():
    off()
    red_on()
    green_on()
    blue_on()

def yellow():
    off()
    green_on()
    blue_on()

def orange():
    off()
    red_on()
    green_on()

def purple():
    off()
    red_on()
    blue_on()

def cycle(seconds=1, full=False):
    off()
    red()
    time.sleep(seconds)
    if full:
        purple()
        time.sleep(seconds)
    blue()
    time.sleep(seconds)
    if full:
        yellow()
        time.sleep(seconds)
    green()
    time.sleep(seconds)
    if full:
        orange()
        time.sleep(seconds)
        white()
        time.sleep(seconds)
    off()
