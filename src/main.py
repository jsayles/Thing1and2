import time
import socket
from machine import Pin, Timer

from core import PRESS, RELEASE, Thingnet
from utils import send_value, watch_for_value


thingnet = None

# LEDs to indicate local and remote activity
local_led = None
remote_led = None


#####################################################################
# Handler Functions
#####################################################################


''' Called when the button is pressed. '''
def local_handler(pin):
    if not thingnet:
        # Do nothing!
        return
    value = pin.value()
    if value == PRESS:
        local_led.on()
    else:
        local_led.off()
    thingnet.send_value(remote_address, value)


# ''' Called when a button press action comes in from the network.'''
# def remote_handler(value):
#     if value == PRESS:
#         remote_led.on()
#         vibe.on()
#     else:
#         remote_led.off()
#         vibe.off()


# ''' Called periodicly to check the network status. '''
# def timer_handler(timer):
#     print("Checking THINGNET Connectivity")
#     if not network_interface:
#         print("  Interface not initialized!")
#         return
#     if network_interface.isconnected():
#         print("  Connected!")
#         main_led.red_off()
#     else:
#         print("  Not Connected!")
#         main_led.red_on()


#####################################################################
# Main Program
#####################################################################

# Hardware Test
main_led.cycle_on(.2)
vibe.pulse(seconds=.2)

# Determine the local and remote LEDs
if I_AM_THING1:
    local_led = blue_led
    remote_led = green_led
else:
    local_led = green_led
    remote_led = blue_led

# Hook up our button to the local handler
button.irq(handler=local_handler, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# Fire up our Network
thingnet = Thingnet(THING_ID, WIFI_SSID, WIFI_PASS, IP_RANGE)

# Main Loop
while True:
    main_led.on()
    thingnet.start()

    main_led.red()
    thingnet.wait_until_connected()

    main_led.orange()
    thingnet.open_incoming_socket()

    main_led.off()
    try:
        while True:
            # Blocking call to wait for a value
            value = thingnet.receive_value()
            if value == PRESS:
                remote_led.on()
                vibe.on()
            else:
                remote_led.off()
                vibe.off()
    except Exception as e:
        print("Lost connection: %s" % str(e))
    finally:
        thingnet.close_incoming_socket()

    # A small delay before we try again
    time.sleep(1.0)


# Start a timer to watch our network
# Timer(-1).init(period=1000, callback=timer_handler, mode=Timer.PERIODIC)


# Listen for values coming in over the network
# watch_for_value(local_address, remote_handler)
