from socket import *
from time import ctime

host = ''
port = 21567
BUFSIZ = 1024
ADDR = (host, port)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpClisock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpClisock.recv(BUFSIZ)
        if not data:
            break
        tcpClisock.send(('[%s] %s' %(ctime(), data)).encode())

    tcpClisock.close()
tcpSerSock.close()