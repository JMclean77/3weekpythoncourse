import socket

host = '127.0.0.1'  # Server's hostname or IP address
port = 65432  # Port used by the server

 # Create a socket (clientSocket) to connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c :
    c.connect((host, port))

 # Send a request to the server
    while True:
        request = input("Enter your request: ")
        if request.lower() == "exit":
            print("Closing the connection")
            break
        c.send(request.encode())


     # Read the reply from the server
        reply = c.recv(1024).decode()
        if not reply:
            print("Server closed")
            break

     # Close the client socket
    c.close()





