import socket
from machine import Pin, Timer

from utils import send_value, watch_for_value


# Network Variables
remote_address = None
local_address = None
network_interface = None
thing1_addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
thing2_addr = socket.getaddrinfo(THING2_IP, THING2_PORT)[0][-1]


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
    # Send the value over the network
    send_value(remote_address, pin.value())


''' Called when a button press action comes in from the network.'''
def remote_handler(value):
    if value == 0:
        vibe.on()
    else:
        vibe.off()


''' Called periodicly to check the network status. '''
def timer_handler(timer):
    print("Checking THINGNET Connectivity")
    print("network_interface: %s" % network_interface)
    if not network_interface:
        return
    print("isconnected: %s" % network_interface.isconnected())
    if network_interface.isconnected():
        main_led.red_off()
    else:
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
if I_AM_THING1:
    local_address = thing1_addr
    remote_address = thing2_addr
    network_interface = create_thingnet()
else:
    local_address = thing2_addr
    remote_address = thing1_addr
    network_interface = join_thingnet()

# Start a timer to watch our network
Timer(-1).init(period=2000, callback=timer_handler, mode=Timer.PERIODIC)

# Hook up our button to the local handler
button.irq(handler=local_handler, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# Listen for values coming in over the network
watch_for_value(remote_address, remote_handler)
