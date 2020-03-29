import time
import network
import socket
import errno

from core import THING1, THING2


class Thingnet:

    def __init__(self, thing_id, ssid, passwd, ip_range):
        self.thing_id = thing_id
        self.ssid = ssid
        self.passwd = passwd

        # Calculate the address for Thing1
        split_ip = ip_range.split('.')
        split_ip[3] = str(THING1)
        self.thing1_ip = ".".join(split_ip)
        self.thing1_port = 8080 + THING1
        self.thing1_address = socket.getaddrinfo(self.thing1_ip, self.thing1_port)[0][-1]

        # Calculate the ip for Thing2
        split_ip[3] = str(THING2)
        self.thing2_ip = ".".join(split_ip)
        self.thing2_port = 8080 + THING2
        self.thing2_address = socket.getaddrinfo(self.thing2_ip, self.thing2_port)[0][-1]

        # Network Variables
        self.network_interface = None
        self.incoming_socket = None
        self.remote_address = None
        self.local_address = None

    ''' Create an access point for THINGNET. '''
    def create_thingnet(self):
        print("Turning on THINGNET (SSID:  %s)" % self.ssid)
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid=self.ssid, password=self.passwd, authmode=3, channel=11, hidden=1)
        ap.ifconfig((self.thing1_ip, '255.255.255.0', self.thing1_ip, '8.8.8.8'))
        return ap

    ''' Join the THINGNET network. '''
    def join_thingnet(self):
        print("Connecting to THINGNET (SSID: %s)" % self.ssid)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.passwd)
        wlan.ifconfig((self.thing2_ip, '255.255.255.0', self.thing1_ip, '8.8.8.8'))
        return wlan

    ''' Turn off all network interfaces. '''
    def stop(self):
        network.WLAN(network.STA_IF).active(False)
        network.WLAN(network.AP_IF).active(False)
        self.network_interface = None

    ''' Start up our network. '''
    def start(self):
        # No good start comes before a stop
        self.stop()

        if self.thing_id == THING1:
            self.local_address = self.thing1_address
            self.remote_address = self.thing2_address
            self.network_interface = self.create_thingnet()
        else:
            self.network_interface = self.join_thingnet()
            self.local_address = self.thing2_address
            self.remote_address = self.thing1_address

    def wait_until_connected(self):
        if not self.network_interface:
            raise Exception("Network not started.  Call start()")
        while not self.network_interface.isconnected():
            time.sleep(0.6)
        return True

    def open_incoming_socket(self):
        sock = socket.socket()
        # sock.settimeout(timeout)
        # sock.setblocking(False)
        # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        sock.setblocking(True)
        sock.bind(self.local_address)
        sock.listen(1)

    def close_incoming_socket(self):
        if self.incoming_socket:
            self.incoming_socket.close()

    def receive_value(self):
        if not self.incoming_socket:
            raise Exception("No incoming socket established!")
        value = -1
        client = None
        try:
            client, client_address = self.incoming_socket.accept()
            print("Client connected from %s:%d" % client_address)
            # client_file = client.makefile('rwb', 0)
            # line = client_file.readline()
            line = client.readline()
            if line[:6] == b'VALUE:':
                value = int(line[6:])
            client.send("OK")
            print("   Recieved Value: %d" % value)
        # except Exception as e:
        #     # if e.args[0] == errno.ETIMEDOUT:
        #     #     print("  Timeout!")
        #     print("  Problem receiving: %s" % str(e))
        finally:
            if client:
                client.close()
        return value

    def send_value(self, value):
        msg = "VALUE:%d" % value
        print("Sending '%s' to %s:%d" % (msg, self.remote_address[0], self.remote_address[1]))
        outgoing_socket = socket.socket()
        try:
            outgoing_socket.connect(self.remote_address)
            outgoing_socket.send(bytes(msg+"\r\n\r\n", 'utf8'))
            return_msg = str(outgoing_socket.recv(64), 'utf8')
            if return_msg == "OK":
                print("  Message Received!")
            else:
                print("  Error: '%s'" % return_msg)
        except Exception as e:
            print("  Problem sending: %s" % str(e))
        finally:
            outgoing_socket.close()
