import time
import settings
import machine


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
