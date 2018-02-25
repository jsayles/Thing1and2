import network
import Settings


# Access Point Interface (creating a wifi network)
def create(ip_address=None):
    if not ip_address:
        ip_address = settings.THING1_IP

    print("Turning on Thing Net (SSID:  %s)" % settings.WIFI_ESSID)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=settings.WIFI_ESSID, password=settings.WIFI_PASSWD, authmode=3, channel=11, hidden=1)
    ap.ifconfig((ip_address, '255.255.255.0', ip_address, '8.8.8.8'))


def join(ip_address=None):
    if not ip_address:
        ip_address = settings.THING1_IP

    print("Connecting to Thing Net (SSID: %s)" % settings.WIFI_ESSID)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(settings.WIFI_ESSID, settings.WIFI_PASSWD)
    wlan.ifconfig((settings.THING2_IP, '255.255.255.0', settings.THING1_IP, '8.8.8.8'))
