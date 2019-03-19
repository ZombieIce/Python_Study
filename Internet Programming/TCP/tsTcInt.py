from socket import *

host = '127.0.0.1'    # or 'localhost'
port = 21567
BUFSIZ = 1024
ADDR = (host, port)

tcpClisock = socket(AF_INET, SOCK_STREAM)
tcpClisock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpClisock.send(data.encode())
    data = tcpClisock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

tcpClisock.close()