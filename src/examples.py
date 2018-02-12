# Access Point Interface (creating a wifi network)
# https://docs.micropython.org/en/latest/esp8266/library/network.html
import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='thingnet', password='uPy12345678', authmode=3, channel=11, hidden=1)
ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
# ap.ifconfig()

# Station Interface (connecting to wifi)
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('thingnet', 'uPy12345678')
wlan.ifconfig(('192.168.4.2', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
# wlan.scan()             # scan for access points
# wlan.isconnected()      # check if the station is connected to an AP
# wlan.config('mac')      # get the interface's MAC adddress
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses


# Haptic Feedback
import board
import bitbangio
import adafruit_drv2605
i2c = bitbangio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)
drv.use_ERM()
drv.set_waveform(14)
drv.play()

# Button Interupt
from machine import Pin
def callback(p):
     print('%s changed to %d', (p, p.value()))
p2 = Pin(2, Pin.IN)
p2_irq = p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
