# Hook up our button interupt
def send_value(to_addr, value):
    import socket
    msg = "VALUE:%d" % value
    print("Sending '%s' to '%s'" % (msg, to_addr))
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

def watch_for_value(my_addr, callback):
    import socket
    s = socket.socket()
    s.bind(my_addr)
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
        callback(line)
