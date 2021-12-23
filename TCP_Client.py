from socket import socket

clientSocket = socket()
host = "127.0.0.1"
port = 12345
clientSocket.connect((host, port))
clientSocket.close()