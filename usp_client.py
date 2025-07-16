import socket

client_socket= socket.socket()

host = socket.gethostname()

client_socket.connect((host, 5533))

print("Connection successfully established")

client_socket.close()

