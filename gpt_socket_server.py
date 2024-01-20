"""Prompt:
Help me write a simple TCP server using sockets in Python. 
// The server must be able to run on a windows compuer. 
// The server will listen for incomming connections from devices trying to connect with it. 
// Devices trying to connect with it must use a passcode "1234" in order to connect with the server. 
// On successfull connection the recipient will receive a "Hello" message.
// Mobile device must be able to connect to the server using the browser app on their phones.
"""

import socket

def start_server():
    print("Starting Server") # Added by me
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 12345))
    serversocket.listen(5) # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print(f"Received connection from {address}")
            if buf.decode("utf-8") == "1234":
                print("Passcode accepted")
                connection.send(bytes("Hello", "utf-8"))
            else:
                print("Incorrect passcode")
                connection.send(bytes("Incorrect passcode", "utf-8"))
            connection.close()

if __name__ == "__main__":
    start_server()
    print("Program end.")