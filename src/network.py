# Hook up our button interupt
def send_value(to_addr, value):
    import socket
    msg = "VALUE:%d" % value
    print("Sending '%s' to '%s'" % msg, to_addr)
    s = socket.socket()
    s.connect(to_addr)
    s.send(bytes(msg+"\r\n\r\n", 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
