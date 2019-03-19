from socket import *
from time import ctime

host = ''
port = 21567
BUFSIZ = 1024
ADDR = (host, port)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' %(ctime(), data)).encode(), addr)
    print('%s received from and returned to: %s'% (data, addr))

udpSerSock.close()
