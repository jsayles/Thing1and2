import time
import socket
import machine

WIFI_ESSID = "thingnet"
WIFI_PASSWD = "uPy12345678"

THING1_IP = "192.168.4.1"
THING1_PORT = 8081
THING2_IP = "192.168.4.2"
THING2_PORT = 8082

PIN_RED = 16
PIN_BLUE = 12
PIN_GREEN = 13
PIN_BUTTON = 2
PIN_VIBE = 14
PIN_VIBE_LED = 0

# Addresses for Thing1 and Thing2
thing1_addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
thing2_addr = socket.getaddrinfo(THING2_IP, THING2_PORT)[0][-1]

# Setup our hardware
red_led = machine.Pin(PIN_RED, machine.Pin.OUT, value=1)
blue_led = machine.Pin(PIN_BLUE, machine.Pin.OUT, value=1)
green_led = machine.Pin(PIN_GREEN, machine.Pin.OUT, value=1)
button = machine.Pin(PIN_BUTTON, machine.Pin.IN, machine.Pin.PULL_UP)
vibe = machine.Pin(PIN_VIBE, machine.Pin.OUT, value=0)
vibe_led = machine.Pin(PIN_VIBE_LED, machine.Pin.OUT, value=1)

def hardware_test():
    import led
    import vibe
    led.cycle()
    led.pulse()
