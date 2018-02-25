import thingnet
import settings
import machine
import network
import socket
import time
import vibe
import led

from utils import send_value, watch_for_value


# Turn on Thing Net
led.red()
thingnet.create(settings.THING1_IP)
led.green()
time.sleep(1)
led.off()

# Hook up our button interupt to send the value over to Thing2
def button_handler(pin):
    send_value(settings.thing2_addr, pin.value())
trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING
settings.button.irq(trigger=trigger, handler=button_handler)

# Listen for values comming from Thing2
def thing2_watcher(msg):
    print("Message from Thing2: '%s'" % msg)
    vibe.pulse(.5)
watch_for_value(settings.thing1_addr, thing2_watcher)
