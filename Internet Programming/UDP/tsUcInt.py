from socket import *

host = 'localhost'
port = 21567
BUFSIZ = 1024
ADDR = (host, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print('client recvfrom', data, ADDR)
udpCliSock.close()