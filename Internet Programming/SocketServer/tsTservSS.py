import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('New Connection:', self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data: break
            print('Client data:', data.decode())
            self.request.send(data)


if __name__ == "__main__":
    host, port = '127.0.0.1', 21567
    s = socketserver.ThreadingTCPServer((host, port), MyServer)
    s.serve_forever()
