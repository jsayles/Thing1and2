#####################################################################
# Main program run after Boot
#####################################################################

import time
import machine

# Hardware Test
power_led.off()
main_led.cycle()
vibe.pulse()
power_led.on()

# Hook up our button to vibe when pressed
def button_handler(pin):
    if pin.value() == 0:
        vibe.on()
    else:
        vibe.off()
button.irq(handler=button_handler, trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)
