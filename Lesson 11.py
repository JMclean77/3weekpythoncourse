import socket

# socket.getaddrinfo
# socket.gethostbyname
# socket.gethostname
#
# print(socket.gethostbyname(socket.gethostname()))
# print(socket.getaddrinfo(socket.gethostname(), 1111))
#

# socket.socket()
# hostname=socket.gethostname()
# print(hostname)
#
# google= socket.gethostbyname("www.google.com")
# print(google)
#
# googleweb= "www.google.com"
# gport= 80
#
# ex2= socket.getaddrinfo(googleweb,gport)
# print(ex2)
#
# s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.connect((google,gport))
#     print("Connection established")
# except socket.error as msg:
#     print(msg)
#
# client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     client_socket.connect(("google.com", 80))
#     print("Connected")
#
#     host= client_socket.getsockname()
#     print(host)
#
# except Exception as e:
#     print(e)
#
# client_socket.close()


hostname= socket.gethostname()
print(hostname)

hostnameip= socket.gethostbyname(hostname)
print(hostnameip)

google= "www.google.com"
port= 80

get_google= socket.gethostbyname(google)
print(get_google)

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((google, port))
print(s)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((google, port))

print(client_socket)
client_socket.close()