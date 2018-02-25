import thingnet
import settings
import machine
import network
import socket
import time
import led

from utils import hardware_test, send_value, watch_for_value


# Test the hardware
hardware_test()

# Turn on Thing Net
led.red()
thingnet.create(settings.THING1_IP)
led.green()
time.sleep(1)
led.off()

# Hook up our button interupt to send the value over to Thing2
def button_handler(pin):
    value = pin.value()
    if value == 0:
        led.blue_on()
    else:
        led.blue_off()
    send_value(settings.thing2_addr, value)
settings.button.irq(handler=button_handler, trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)

# Listen for values comming from Thing2
def thing2_watcher(thing2_value):
    # print("Message from Thing2: '%s'" % msg)
    if thing2_value == 0:
        led.green_on()
        settings.vibe.on()
    else:
        led.green_off()
        settings.vibe.off()
watch_for_value(settings.thing1_addr, thing2_watcher)
