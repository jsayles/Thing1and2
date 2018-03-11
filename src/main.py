import socket
from machine import Pin, Timer

from core import PRESS, RELEASE, Thingnet
from utils import send_value, watch_for_value


# Network Variables
network_interface = None
remote_address = None
local_address = None

# LEDs to indicate local and remote activity
local_led = None
remote_led = None


#####################################################################
# Helper Functions
#####################################################################


def create_thingnet():
    print("Turning on THINGNET (SSID:  %s)" % WIFI_ESSID)
    network.WLAN(network.STA_IF).active(False)
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=WIFI_ESSID, password=WIFI_PASSWD, authmode=3, channel=11, hidden=1)
    ap.ifconfig((THING1_IP, '255.255.255.0', THING1_IP, '8.8.8.8'))
    return ap


def join_thingnet():
    print("Connecting to THINGNET (SSID: %s)" % WIFI_ESSID)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_ESSID, WIFI_PASSWD)
    wlan.ifconfig((THING2_IP, '255.255.255.0', THING1_IP, '8.8.8.8'))
    return wlan



#####################################################################
# Handler Functions
#####################################################################


''' Called when the button is pressed. '''
def local_handler(pin):
    value = pin.value()
    if value == PRESS:
        local_led.on()
    else:
        local_led.off()
    send_value(remote_address, value)


''' Called when a button press action comes in from the network.'''
def remote_handler(value):
    if value == PRESS:
        remote_led.on()
        vibe.on()
    else:
        remote_led.off()
        vibe.off()


''' Called periodicly to check the network status. '''
def timer_handler(timer):
    print("Checking THINGNET Connectivity")
    if not network_interface:
        print("  Interface not initialized!")
        return
    if network_interface.isconnected():
        print("  Connected!")
        main_led.red_off()
    else:
        print("  Not Connected!")
        main_led.red_on()


#####################################################################
# Main Program
#####################################################################

# Hardware Test
power_led.off()
main_led.cycle(seconds=.2)
vibe.pulse(seconds=.2)
power_led.on()
red_led.on()

# Fire up our Network
thingnet = Thingnet(THING_ID, WIFI_SSID, WIFI_PASS, IP_RANGE)
if I_AM_THING1:
    local_address = thingnet.thing1_addr
    remote_address = thingnet.thing2_addr
    network_interface = thingnet.create_thingnet()
    local_led = blue_led
    remote_led = green_led
else:
    local_address = thingnet.thing2_addr
    remote_address = thingnet.thing1_addr
    network_interface = thingnet.join_thingnet()
    local_led = green_led
    remote_led = blue_led

# Start a timer to watch our network
Timer(-1).init(period=1000, callback=timer_handler, mode=Timer.PERIODIC)

# Hook up our button to the local handler
button.irq(handler=local_handler, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# Listen for values coming in over the network
watch_for_value(local_address, remote_handler)
