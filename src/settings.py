import time
import socket
import machine

WIFI_ESSID = "thingnet"
WIFI_PASSWD = "uPy12345678"

# Addresses for Thing1 and Thing2
THING1_IP = "192.168.4.1"
THING1_PORT = 8081
THING2_IP = "192.168.4.2"
THING2_PORT = 8082
thing1_addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
thing2_addr = socket.getaddrinfo(THING2_IP, THING2_PORT)[0][-1]

# Setup our hardware
power_led = machine.Pin(0, machine.Pin.OUT, value=0)
red_led = machine.Pin(16, machine.Pin.OUT, value=1)
blue_led = machine.Pin(12, machine.Pin.OUT, value=1)
green_led = machine.Pin(13, machine.Pin.OUT, value=1)
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
vibe = machine.Pin(14, machine.Pin.OUT, value=0)
