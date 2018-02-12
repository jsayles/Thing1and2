import settings
import machine
import socket

# Setup our hardware
red_led = machine.Pin(settings.PIN_RED, machine.Pin.OUT)
blue_led = machine.Pin(settings.PIN_BLUE, machine.Pin.OUT)
green_led = machine.Pin(settings.PIN_GREEN, machine.Pin.OUT)
button = machine.Pin(settings.PIN_BUTTON, machine.Pin.IN, machine.Pin.PULL_UP)

# Access Point Interface (creating a wifi network)
print("Turning on the Access Point (%s)" % settings.WIFI_ESSID)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=settings.WIFI_ESSID, password=settings.WIFI_PASSWD, authmode=3, channel=11, hidden=1)
ap.ifconfig((settings.THING1_IP, '255.255.255.0', settings.THING1_IP, '8.8.8.8'))

# Addresses for Thing1 and Thing2
thing1_addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
thing2_addr = socket.getaddrinfo(THING2_IP, THING2_PORT)[0][-1]

# Hook up our button interupt
def send_button(pin):
    s = socket.socket()
    s.connect(thing2_addr)
    s.send(bytes("VALUE:%d\r\n\r\n" % pin.value(), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=send_button)

# Start our HTTP server to listen for Thing2
addr = socket.getaddrinfo(THING1_IP, THING1_PORT)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    cl.send("OK")
    cl.close()
