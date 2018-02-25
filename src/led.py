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


def red():
    settings.red_led.off()
    settings.blue_led.on()
    settings.green_led.on()


def blue():
    settings.red_led.on()
    settings.blue_led.off()
    settings.green_led.on()


def green():
    settings.red_led.on()
    settings.blue_led.on()
    settings.green_led.off()


def white():
    settings.red_led.off()
    settings.blue_led.off()
    settings.green_led.off()


def yellow():
    settings.red_led.on()
    settings.blue_led.off()
    settings.green_led.off()


def orange():
    settings.red_led.off()
    settings.blue_led.on()
    settings.green_led.off()


def purple():
    settings.red_led.off()
    settings.blue_led.off()
    settings.green_led.on()


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
