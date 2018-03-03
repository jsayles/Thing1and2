import socket
import machine
import network

from core import HIGH, LOW, LED, RGB_LED, Vibe


# Hardware Settings
power_pin = machine.Pin(0, machine.Pin.OUT, value=0)
power_led = LED(power_pin, on_value=HIGH, start_on=True)
red_pin = machine.Pin(16, machine.Pin.OUT, value=1)
red_led = LED(red_pin, on_value=LOW)
green_pin = machine.Pin(13, machine.Pin.OUT, value=1)
green_led = LED(green_pin, on_value=LOW)
blue_pin = machine.Pin(12, machine.Pin.OUT, value=1)
blue_led = LED(blue_pin, on_value=LOW)
main_led = RGB_LED(red_led, green_led, blue_led)
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
vibe_pin = machine.Pin(14, machine.Pin.OUT, value=0)
vibe = Vibe(vibe_pin)

# Network Settings
WIFI_ESSID = "thingnet"
WIFI_PASSWD = "uPy12345678"
THING1_IP = "192.168.4.1"
THING1_PORT = 8081
THING2_IP = "192.168.4.2"
THING2_PORT = 8082
THING1_MAC = b'\x18\xfe4\xd3\x81\xd5'
THING2_MAC = b'\x18\xfe4\xd3\x89\x1a'
thing1_addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
thing2_addr = socket.getaddrinfo(THING2_IP, THING2_PORT)[0][-1]

# Who Am I?!?
I_AM_THING1 = False
I_AM_THING2 = False
my_mac_address = network.WLAN().config('mac')
if my_mac_address == THING1_MAC:
    # I Am Thing1 - Blue
    I_AM_THING1 = True
    vibe.set_status_led(blue_led)
if my_mac_address == THING2_MAC:
    # I am Thing2 - Green
    I_AM_THING2 = True
    vibe.set_status_led(green_led)

# Hardware Test
power_led.off()
main_led.cycle()
vibe.pulse()
power_led.on()
