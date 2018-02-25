import time
import settings

# PWM Settings
# pwm = machine.PWM(machine.Pin(PIN_VIBE))
# How fast the PWM signal is turned on and off
# 60 = 60 times per second
# pwm.freq(60)
# Percent of time that the signal is on vs. off,
# Range of 0 to 1023
# pwm.duty(1023)
# Turn off the pin
# pwm.duty(0)

def pulse_vibe(seconds=1):
    settings.vibe_led.off() # Off = Lighted
    settings.vibe.on()
    time.sleep(seconds)
    settings.vibe_led.on() # on = Not lighted
    settings.vibe.off()
