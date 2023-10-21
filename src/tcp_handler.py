import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()
