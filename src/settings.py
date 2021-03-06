import network
from machine import Pin

from core import LED, RGB_LED, Vibe
from core import THING1, THING2, HIGH, LOW


# Hardware Settings
power_pin = Pin(0, Pin.OUT, value=0)
power_led = LED(power_pin, on_value=HIGH, start_on=True)
red_pin = Pin(16, Pin.OUT, value=1)
red_led = LED(red_pin, on_value=LOW)
green_pin = Pin(13, Pin.OUT, value=1)
green_led = LED(green_pin, on_value=LOW)
blue_pin = Pin(12, Pin.OUT, value=1)
blue_led = LED(blue_pin, on_value=LOW)
main_led = RGB_LED(red_led, green_led, blue_led)
button = Pin(2, Pin.IN, Pin.PULL_UP)
vibe_pin = Pin(14, Pin.OUT, value=0)
vibe = Vibe(vibe_pin)

# Network Settings
WIFI_SSID = "thingnet"
WIFI_PASS = "uPy12345678"
IP_RANGE = "192.168.4.1"
THING1_MAC = b'\x18\xfe4\xd3\x81\xd5'
THING2_MAC = b'\x18\xfe4\xd3\x89\x1a'

# Who Am I?!?
THING_ID = None
I_AM_THING1 = False
I_AM_THING2 = False
my_mac_address = network.WLAN().config('mac')
if my_mac_address == THING1_MAC:
    # I Am Thing1
    print("I am Thing1!")
    I_AM_THING1 = True
    THING_ID = THING1
if my_mac_address == THING2_MAC:
    # I am Thing2
    print("I am Thing2!")
    I_AM_THING2 = True
    THING_ID = THING2
