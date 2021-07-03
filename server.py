import socketserver

class PingTracker(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        utf8resp = str(self.data,'utf-8')
        # print("Data:\n{}".format(utf8resp))
        headers = {}
        for header in utf8resp.splitlines()[1:-1]:
            if header != '':
                pair = header.split(':')
                headers[pair[0].strip()] = pair[1].strip()
            # print(header)

        print(utf8resp[len(utf8resp)-int(headers['Content-Length']):]+"\n\n")
        self.request.sendall(self.data+ b'Recieved\n')
        self.request.close()
s = socketserver.TCPServer(('127.0.0.1',8080),PingTracker)
try:
    s.serve_forever()
except KeyboardInterrupt as e:
    print("Shutting down")
    s.shutdown()