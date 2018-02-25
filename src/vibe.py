#####################################################################
# Functions to operate the vibrating motor
#####################################################################

import time
import settings

# PWM Settings for adjustable vibe strength
# pwm = machine.PWM(machine.Pin(PIN_VIBE))
# How fast the PWM signal is turned on and off
# 60 = 60 times per second
# pwm.freq(60)
# Percent of time that the signal is on vs. off,
# Range of 0 to 1023
# pwm.duty(1023)
# Turn off the pin
# pwm.duty(0)

def on():
    # settings.red_led.off() # Off = Lighted
    settings.vibe.on()


def off():
    # settings.red_led.on() # on = Not lighted
    settings.vibe.off()


def pulse(seconds=.5):
    on()
    time.sleep(seconds)
    off()
