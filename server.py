import socket
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        data = self.request.recv(1024 * 8).strip()
        data = data.decode('utf-8')
        print(f'Message from {self.client_address}')
        print(data)
        data = data.split(';')
        addr = data[1]
        ip, port = addr.split(':')
        port = int(port)
        if data[0].lower() == 'check':
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((ip, port))
                message = f'{ip}:{port};OK'
            except socket.error:
                message = f'{ip}:{port};BAD'
            self.request.sendall(bytes(message, 'utf-8'))
        elif data[0].lower() == 'move':
            message = f'{ip}:{port};{data[2]};{data[3]}'
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(60 * 60)
            sock.connect((ip, port))
            sock.sendall(bytes(message, 'utf-8'))
            self.request.sendall(sock.recv(1024))



if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 1111
    print(f'Your addr is {HOST}:{PORT}')
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
