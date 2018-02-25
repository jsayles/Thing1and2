import settings
import machine
import network
import socket
import time
import vibe
import led

from utils import send_value, watch_for_value


# Start out with our LED red
led.red()

# Access Point Interface (creating a wifi network)
print("Turning on the Access Point (%s)" % settings.WIFI_ESSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=settings.WIFI_ESSID, password=settings.WIFI_PASSWD, authmode=3, channel=11, hidden=1)
ap.ifconfig((settings.THING1_IP, '255.255.255.0', settings.THING1_IP, '8.8.8.8'))

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

# Turn the LED green to indicate we're ready to go
led.green()
time.sleep(1)
led.off()
