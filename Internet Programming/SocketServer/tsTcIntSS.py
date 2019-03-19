from socket import *

host = 'localhost'
port = 21567
BUFSIZ = 1024
ADDR = (host, port)

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ADDR)

while True:
    msg = input('> ').strip()
    if not msg:break
    if msg == 'quit':break
    tcp_client.sendall(msg.encode('utf-8'))
    data = tcp_client.recv(BUFSIZ)
    print('received from serve is: ', data.decode('utf-8'))

tcp_client.close()
