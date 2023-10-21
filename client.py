import socket

HOST, PORT = "194.87.93.169", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        data = input('Input: ')
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
