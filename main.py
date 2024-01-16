#!/usr/bin/python3
import socket

# base setup fro socket server
socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# setting up host details and port
host = socket.gethostname()
port = 445

# binding and listening. 

socket_server.bind((host, port)) # binding host and port
socket_server.listen(4) # Ammount of connection that can listen in brackets


while True:
    client_socket, address = socket_server.accept()
    print(f"received connection from {address}.")
    client_socket.send("Thanks for connecting\n")
    client_socket.close()