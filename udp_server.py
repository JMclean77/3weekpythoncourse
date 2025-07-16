import socket

server_socket = socket.socket()

host= socket.gethostname()

port = 5533

server_socket.bind((host, port))

server_socket.listen(1)

conn , addr = server_socket.accept()

print(f"Connected to {addr}")