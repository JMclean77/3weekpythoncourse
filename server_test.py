import socket

import requests

host = "127.0.0.1"  # Localhost
port = 65432  # Port to listen on

# Create a socket (welcomeSocket) to listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print(f"Serveris listening on port {port}...")
    connectionSocket, addr = s.accept()
    print(f"Connected to {addr}")

# Accept a connection from a client


# Read the request from the client
request = connectionSocket.recv(1024).decode()
if not request:
    print("Connection closed")

connectionSocket.sendall(request.encode())
print(f"Received request: {request}")
reply = "This is the server"
connectionSocket.sendall(reply.encode())

# Close the connection
connectionSocket.close()