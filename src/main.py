#####################################################################
# Functions to operate the RGB led
#
# Note:  LED is wired high so bring led pin low to turn on.
#####################################################################

import time
import machine
import settings

# red_led = machine.Pin(16, machine.Pin.OUT)
# blue_led = machine.Pin(12, machine.Pin.OUT)
# green_led = machine.Pin(13, machine.Pin.OUT)
# button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
# i = 1
# while(True):
#     red_led.on()
#     blue_led.on()
#     green_led.on()
#     if i == 1:
#         red_led.off()
#     elif i == 2:
#         blue_led.off()
#     else:
#         green_led.off()
#         i = 0
#     time.sleep(1)
#     i = i + 1

settings.hardware_test()
